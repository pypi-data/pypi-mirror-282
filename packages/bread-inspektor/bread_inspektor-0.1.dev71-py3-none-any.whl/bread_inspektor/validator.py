import datetime as dt
import json
from itertools import zip_longest
from pathlib import Path
from typing import Any, Optional, Union

from bread_inspektor import constants, rules
from bread_inspektor.file_utils import CSVData


class ColumnValidation:
    def __init__(self, column_name: str, validation: constants.Validator):
        self.column_name = column_name
        self.validation = validation

    def validate(self, value: Any) -> bool:
        validator_func = self.validation.validator()
        return validator_func(value)


class RowValidation:
    def __init__(self, validation: constants.Validator):
        self.validation = validation

    def validate(self, row: list[Any]) -> bool:
        validator_func = self.validation.validator()
        return validator_func(row)


class SingleFileValidator:
    def __init__(
        self,
        data_format: str,
        file_path: Path,
        column_dtypes: dict,
        nullable_columns: list[str],
        column_validations: list[ColumnValidation],
        row_validations: list[RowValidation],
        csv_header: Optional[list[str]] = None,
        single_error_log_limit: int = 20,
        row_offset: int = 2,
    ) -> None:
        self.issues = []
        self.can_continue = True
        self.data_format = data_format
        self.csv_data_object = self.get_csv_data_object(file_path, csv_header)
        self.column_dtypes = column_dtypes
        self.nullable_columns = nullable_columns
        self.column_validations = column_validations
        self.row_validations = row_validations
        # This param short circuits checking and logging any given issue.
        self.single_error_log_limit = single_error_log_limit
        self.row_offset = row_offset

    def get_csv_data_object(
        self, file_path: Path, csv_header: Optional[list[str]] = None
    ) -> CSVData:
        try:
            csv_data_object = CSVData(file_path, csv_header)
        except FileNotFoundError:
            self.issues.append(
                {
                    "data_format": self.data_format,
                    "issue_type": "file_not_found",
                    "issue_details": {
                        "msg": f"Expected a CSV file in location {file_path}",
                    },
                }
            )
            self.can_continue = False
        except Exception as e:
            self.issues.append(
                {
                    "data_format": self.data_format,
                    "issue_type": "data_loading_failure",
                    "issue_details": {
                        "msg": "Encountered an unexpected error",
                        "error": e,
                    },
                }
            )
            raise
        return csv_data_object

    def validate_column_names(self) -> None:
        expected_cols = [self.csv_data_object.index_col] + [
            *self.column_dtypes.keys()
        ]
        file_cols = self.csv_data_object.header
        if set(expected_cols) != set(file_cols):
            missing_cols = set(expected_cols).difference(set(file_cols))
            extra_cols = set(file_cols).difference(set(expected_cols))
            self.issues.append(
                {
                    "data_format": self.data_format,
                    "issue_type": "column_name_validation",
                    "issue_details": {
                        "columns_missing_from_file": list(missing_cols),
                        "extra_columns_in_file": list(extra_cols),
                    },
                }
            )

    def validate_column_order(self) -> None:
        expected_cols = [self.csv_data_object.index_col] + [
            *self.column_dtypes.keys()
        ]
        file_cols = self.csv_data_object.header
        for i, (exp_col, file_col) in enumerate(
            zip_longest(expected_cols, file_cols, fillvalue="<missing_column>")
        ):
            if exp_col != file_col:
                self.issues.append(
                    {
                        "data_format": self.data_format,
                        "issue_type": "column_order_validation",
                        "issue_details": {
                            "column_number": i,
                            "expected_column_name": exp_col,
                            "column_name_in_file": file_col,
                        },
                    }
                )

    def validate_column_types(self) -> None:
        """At present, this also has the stateful effect of casting column
        values to the defined dtype.
        """
        for i, column in enumerate(self.csv_data_object.header):
            column_can_be_null = column in self.nullable_columns
            if column == self.csv_data_object.index_col:
                valid_column_type = int
            else:
                valid_column_type = self.column_dtypes.get(column)
            if valid_column_type is None:
                self.issues.append(
                    {
                        "data_format": self.data_format,
                        "issue_type": "column_dtype_undefined",
                        "issue_details": {"column": column},
                    }
                )
            for row in self.csv_data_object.data:
                try:
                    if valid_column_type != str:
                        # Convert the data type here
                        # Was that "row[i] + 2" part supposed to be there?
                        if column_can_be_null and (
                            row[i] is None or row[i] == ""
                        ):
                            continue
                        row[i] = valid_column_type(row[i])
                except (ValueError, IndexError):
                    self.issues.append(
                        {
                            "data_format": self.data_format,
                            "issue_type": "column_dtype_validation",
                            "issue_details": {
                                "row_number": row[0] + self.row_offset,
                                "column": column,
                                "uncastable_value": row[i],
                                "intended_type": valid_column_type.__name__,
                            },
                        }
                    )
                except Exception as e:
                    self.issues.append(
                        {
                            "data_format": self.data_format,
                            "issue_type": "column_dtype_validation_misc",
                            "issue_details": {
                                "row_number": row[0],
                                "column": column,
                                "error": e,
                            },
                        }
                    )

    def validate_column_non_nullness(self) -> None:
        for i, column in enumerate(self.csv_data_object.header):
            if column in self.nullable_columns:
                continue
            rows_w_null_col_val = []
            num_null = 0
            continue_checking = True
            for row in self.csv_data_object.data:
                if row[i] is None or row[i] == "":
                    num_null += 1
                    rows_w_null_col_val.append(row[0] + self.row_offset)
                if num_null > self.single_error_log_limit:
                    continue_checking = False
                    break
            if num_null > 0:
                self.issues.append(
                    {
                        "data_format": self.data_format,
                        "issue_type": "required_column_not_null_validation",
                        "issue_details": {
                            "column": column,
                            "rows_where_column_is_null": rows_w_null_col_val,
                            "checked_all_rows": continue_checking,
                        },
                    }
                )

    def validate_column_contents(self) -> None:
        for col_validation in self.column_validations:
            num_errors = 0
            continue_checking = True
            col_name = col_validation.column_name
            failing_rows = []
            try:
                col_index = self.csv_data_object.header.index(col_name)
                for row in self.csv_data_object.data:
                    if not col_validation.validate(row[col_index]):
                        num_errors += 1
                        failing_rows.append(
                            (row[0] + self.row_offset, row[col_index])
                        )
                    if num_errors > self.single_error_log_limit:
                        continue_checking = False
                        break
                if num_errors > 0:
                    self.issues.append(
                        {
                            "data_format": self.data_format,
                            "issue_type": "column_contents_validation",
                            "issue_details": {
                                "column": col_validation.column_name,
                                "validation": (
                                    col_validation.validation.__name__
                                ),
                                "failing_rows_and_values": failing_rows,
                                "checked_all_rows": continue_checking,
                            },
                        }
                    )
            except ValueError:
                self.issues.append(
                    {
                        "data_format": self.data_format,
                        "issue_type": "column_missing",
                        "issue_details": {
                            "column": col_validation.column_name,
                        },
                    }
                )

    def validate_row_contents(self) -> None:
        for row_validation in self.row_validations:
            num_errors = 0
            continue_checking = True
            failing_rows = []
            for row in self.csv_data_object.data:
                if not row_validation.validate(row):
                    num_errors += 1
                    failing_rows.append((row[0] + self.row_offset, row))
                if num_errors > self.single_error_log_limit:
                    continue_checking = False
                    break
            if num_errors > 0:
                self.issues.append(
                    {
                        "data_format": self.data_format,
                        "issue_type": "row_rule_validation",
                        "issue_details": {
                            "rule_descr": row_validation.validation.rule_descr,
                            "validation": row_validation.validation.__name__,
                            "failing_rows_and_values": failing_rows,
                            "checked_all_rows": continue_checking,
                        },
                    }
                )

    def run_single_file_validations(self) -> None:
        validation_funcs = [
            self.validate_column_names,
            self.validate_column_order,
            self.validate_column_types,
            self.validate_column_non_nullness,
            self.validate_column_contents,
            self.validate_row_contents,
        ]
        for validation_func in validation_funcs:
            validation_func()
            if not self.can_continue:
                break


class ChallengerDataValidator:
    COLUMN_DTYPES = {
        "challenger": str,
        "category": str,
        "organization": str,
        "webpage": str,
        "provider_id": str,
        "contact_name": str,
        "contact_email": str,
        "contact_phone": str,
    }
    NULLABLE_COLUMNS = ["webpage", "provider_id", "contact_phone"]
    COLUMN_VALIDATIONS = [
        ColumnValidation("challenger", constants.NonNullableValidator),
        ColumnValidation("category", constants.ChallengerType),
        ColumnValidation("organization", constants.NonNullableValidator),
        ColumnValidation("webpage", constants.WebPageValidator),
        ColumnValidation("provider_id", constants.FccProviderIdValidator),
        ColumnValidation("contact_name", constants.NonNullableValidator),
        ColumnValidation("contact_email", constants.EmailValidator),
        ColumnValidation("contact_phone", constants.PhoneValidator),
    ]
    ROW_VALIDATIONS = [
        RowValidation(rules.ChallengersISPProviderIdRuleValidator),
    ]

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="challenger",
            file_path=file_path,
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
        )
        self.file_validator.run_single_file_validations()


class ChallengesDataValidator:
    COLUMN_DTYPES = {
        "challenge": str,
        "challenge_type": str,
        "challenger": str,
        "challenge_date": str,
        "rebuttal_date": str,
        "resolution_date": str,
        "disposition": str,
        "provider_id": str,
        "technology": int,  # int per the doc, but TechCode might expect strs?
        "location_id": int,
        "unit": str,
        "reason_code": str,
        "evidence_file_id": str,
        "response_file_id": str,
        "resolution": str,
        "advertised_download_speed": float,
        "download_speed": float,
        "advertised_upload_speed": float,
        "upload_speed": float,
        "latency": float,
    }
    NULLABLE_COLUMNS = [
        "challenger",
        "rebuttal_date",
        "provider_id",
        "technology",
        "unit",
        "reason_code",
        "evidence_file_id",
        "response_file_id",
        "resolution",
        "advertised_download_speed",
        "download_speed",
        "advertised_upload_speed",
        "upload_speed",
        "latency",
    ]
    COLUMN_VALIDATIONS = [
        ColumnValidation("challenge", constants.ChallengeIdValidator),
        ColumnValidation("challenge_type", constants.ChallengeType),
        ColumnValidation("challenge_date", constants.DateValidator),
        ColumnValidation("rebuttal_date", constants.DateNullableValidator),
        ColumnValidation("resolution_date", constants.DateNullableValidator),
        ColumnValidation("disposition", constants.DispositionsOfChallenge),
        ColumnValidation("provider_id", constants.FccProviderIdValidator),
        ColumnValidation("technology", constants.TechCode),
        ColumnValidation("location_id", constants.BSLLocationIdValidator),
        ColumnValidation("reason_code", constants.ReasonCode),
        ColumnValidation(
            "evidence_file_id", constants.FileNameNullableValidator
        ),
        ColumnValidation(
            "response_file_id", constants.FileNameNullableValidator
        ),
        ColumnValidation(
            "advertised_download_speed",
            constants.NonNegativeNumberNullableValidator,
        ),
        ColumnValidation(
            "download_speed", constants.NonNegativeNumberNullableValidator
        ),
        ColumnValidation(
            "advertised_upload_speed",
            constants.NonNegativeNumberNullableValidator,
        ),
        ColumnValidation(
            "upload_speed", constants.NonNegativeNumberNullableValidator
        ),
        ColumnValidation(
            "latency", constants.NonNegativeNumberNullableValidator
        ),
    ]
    ROW_VALIDATIONS = [
        RowValidation(
            rules.ChallengesChallengerIdGivenChallengeTypeRuleValidator
        ),
        RowValidation(rules.ChallengesAvailabilityChallengeTypeRuleValidator),
        RowValidation(
            rules.ChallengesResolutionGivenChallengeTypeRuleValidator
        ),
        RowValidation(
            rules.ChallengesAdvertisedDownloadSpeedChallengeTypeRuleValidator
        ),
        RowValidation(rules.ChallengesDownloadSpeedChallengeTypeRuleValidator),
        RowValidation(
            rules.ChallengesAdvertisedUploadSpeedChallengeTypeRuleValidator
        ),
        RowValidation(rules.ChallengesUploadSpeedChallengeTypeRuleValidator),
        RowValidation(rules.ChallengesRebuttalDateAndFileRuleValidator),
        RowValidation(rules.ChallengesLatencyChallengeTypeRuleValidator),
        RowValidation(rules.ChallengesProviderIdChallengeTypeRuleValidator),
        RowValidation(rules.ChallengesTechnologyChallengeTypeRuleValidator),
        RowValidation(rules.ChallengesEvidenceFileChallengeTypeRuleValidator),
        RowValidation(rules.ChallengesChallengeAndRebuttalDateRuleValidator),
        RowValidation(rules.ChallengesChallengeAndResolutionDateRuleValidator),
        RowValidation(rules.ChallengesRebuttalAndResolutionDateRuleValidator),
    ]

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="challenges",
            file_path=file_path,
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
        )
        self.file_validator.run_single_file_validations()


class PostChallengeCAIDataValidator:
    COLUMN_DTYPES = {
        "type": str,
        "entity_name": str,
        "entity_number": int,
        "cms_number": str,
        "frn": str,
        "location_id": str,
        "address_primary": str,
        "city": str,
        "state": str,
        "zip_code": str,
        "longitude": float,
        "latitude": float,
        "explanation": str,
        "need": int,
        "availability": int,
    }
    NULLABLE_COLUMNS = [
        "entity_number",
        "cms_number",
        "frn",
        "location_id",
        "address_primary",
        "city",
        "zip_code",
        "longitude",
        "latitude",
        "explanation",
        "availability",
    ]
    COLUMN_VALIDATIONS = [
        ColumnValidation("type", constants.CAIType),
        ColumnValidation("entity_name", constants.NonNullableValidator),
        ColumnValidation(
            "cms_number", constants.CMSCertificateNullableValidator
        ),
        ColumnValidation("frn", constants.FrnNullableValidator),
        ColumnValidation(
            "location_id", constants.BSLLocationIdNullableValidator
        ),
        ColumnValidation("state", constants.State),
        ColumnValidation("zip_code", constants.ZipNullableValidator),
        ColumnValidation("longitude", constants.LongitudeNullableValidator),
        ColumnValidation("latitude", constants.LatitudeNullableValidator),
        ColumnValidation("need", constants.NonNegativeNumberValidator),
        ColumnValidation(
            "availability", constants.NonNegativeNumberNullableValidator
        ),
    ]

    ROW_VALIDATIONS = [
        RowValidation(rules.PostChallengeCaiCMSValidatorGivenCAIType),
        RowValidation(rules.PostChallengeCaiFRNValidationGivenCAIType),
        RowValidation(rules.PostChallengeCaiLocationValidation),
        RowValidation(rules.PostChallengeCaiExplanationValidationGivenCAIType),
    ]

    DATA_FORMAT = "post_challenge_cai"

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format=self.DATA_FORMAT,
            file_path=file_path,
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
        )
        self.file_validator.run_single_file_validations()


class CAIDataValidator(PostChallengeCAIDataValidator):
    """
    Per the guideline doc this has the same format as post_challenge_cai
    """

    DATA_FORMAT = "cai"


class CAIChallengeDataValidator:
    COLUMN_DTYPES = {
        "challenge": str,
        "challenge_type": str,
        "challenger": str,
        "category_code": str,
        "disposition": str,
        "challenge_explanation": str,
        "type": str,
        "entity_name": str,
        "entity_number": int,
        "cms_number": str,
        "frn": str,
        "location_id": int,
        "address_primary": str,
        "city": str,
        "state": str,
        "zip_code": str,
        "longitude": float,
        "latitude": float,
        "explanation": str,
        "need": int,
        "availability": int,
    }
    NULLABLE_COLUMNS = [
        "category_code",
        "explanation",
        "entity_name",
        "entity_number",
        "cms_number",
        "frn",
        "location_id",
        "address_primary",
        "city",
        "zip_code",
        "longitude",
        "latitude",
        "availability",
        "challenge_explanation",
        "availability",
    ]

    COLUMN_VALIDATIONS = [
        ColumnValidation("challenge", constants.ChallengeIdValidator),
        ColumnValidation("challenge_type", constants.CAIChallengeType),
        ColumnValidation(
            "category_code", constants.CAIRationaleNullableValidator
        ),
        ColumnValidation("disposition", constants.DispositionsOfCAIChallenge),
        ColumnValidation("type", constants.CAIType),
        ColumnValidation(
            "cms_number", constants.CMSCertificateNullableValidator
        ),
        ColumnValidation("frn", constants.FrnNullableValidator),
        ColumnValidation(
            "location_id", constants.BSLLocationIdNullableValidator
        ),
        ColumnValidation("state", constants.State),
        ColumnValidation("zip_code", constants.ZipNullableValidator),
        ColumnValidation("need", constants.NonNegativeNumberValidator),
        ColumnValidation(
            "availability", constants.NonNegativeNumberNullableValidator
        ),
    ]

    ROW_VALIDATIONS = [
        RowValidation(rules.CaiChallengeCaiLocationValidationPostChallenge),
        RowValidation(rules.CaiChallengeCategoryCodeConditionalGivenType),
        RowValidation(rules.CaiChallengeExplanationConditionalTypeC),
        RowValidation(rules.CaiChallengeEntityNameConditionalType),
        RowValidation(rules.CaiChallengeChallengeExplanationConditionalTypeC),
        RowValidation(rules.CaiChallengeCMSConditionalTypeH),
        RowValidation(rules.CaiChallengeFRNGivenType),
    ]

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="cai_challenge",
            file_path=file_path,
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
        )
        self.file_validator.run_single_file_validations()


class PostChallengeLocationDataValidator:
    COLUMN_DTYPES = {
        "location_id": int,
        "classification": int,
    }
    NULLABLE_COLUMNS = []
    COLUMN_VALIDATIONS = [
        ColumnValidation("location_id", constants.BSLLocationIdValidator),
        ColumnValidation(
            "classification", constants.LocationClassificationCode
        ),
    ]
    ROW_VALIDATIONS = []

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="post_challenge_locations",
            file_path=file_path,
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
        )
        self.file_validator.run_single_file_validations()


class UnservedDataValidator:
    COLUMN_DTYPES = {"location_id": int}
    NULLABLE_COLUMNS = []
    COLUMN_VALIDATIONS = [
        ColumnValidation("location_id", constants.BSLLocationIdValidator),
    ]
    ROW_VALIDATIONS = []

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="unserved",
            file_path=file_path,
            csv_header=["location_id"],
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
            row_offset=1,
        )
        self.file_validator.run_single_file_validations()


class UnderservedDataValidator:
    COLUMN_DTYPES = {"location_id": int}
    NULLABLE_COLUMNS = []
    COLUMN_VALIDATIONS = [
        ColumnValidation("location_id", constants.BSLLocationIdValidator),
    ]
    ROW_VALIDATIONS = []

    def __init__(
        self, file_path: Path, single_error_log_limit: int = 20
    ) -> None:
        self.file_validator = SingleFileValidator(
            data_format="underserved",
            file_path=file_path,
            csv_header=["location_id"],
            column_dtypes=self.COLUMN_DTYPES,
            nullable_columns=self.NULLABLE_COLUMNS,
            column_validations=self.COLUMN_VALIDATIONS,
            row_validations=self.ROW_VALIDATIONS,
            single_error_log_limit=single_error_log_limit,
            row_offset=1,
        )
        self.file_validator.run_single_file_validations()


class BEADChallengeDataValidator:
    EXPECTED_DATA_FORMATS = [
        "unserved",
        "underserved",
        "cai",
        "challengers",
        "challenges",
        "cai_challenges",
        "post_challenge_locations",
        "post_challenge_cai",
    ]
    DATA_FORMAT_VALIDATORS = {
        "cai": CAIDataValidator,
        "cai_challenges": CAIChallengeDataValidator,
        "challenges": ChallengesDataValidator,
        "challengers": ChallengerDataValidator,
        "post_challenge_cai": PostChallengeCAIDataValidator,
        "post_challenge_locations": PostChallengeLocationDataValidator,
        "unserved": UnservedDataValidator,
        "underserved": UnderservedDataValidator,
    }

    def __init__(
        self,
        data_directory: Path,
        expected_data_formats: Union[str, list[str]] = "*",
        results_dir: Optional[Path] = None,
    ):
        self.issues = []
        if expected_data_formats == "*":
            expected_data_formats = self.EXPECTED_DATA_FORMATS
        self.expected_data_formats = expected_data_formats
        self.missing_data_formats = set()
        self.data_dir = Path(data_directory).resolve()
        self.results_dir = results_dir
        self.setup_result_logging()
        self.set_data_format_to_path_map()
        self.check_for_missing_formats()
        self.run_data_validations()

    def _get_data_format(self, file_path: Path) -> str:
        return file_path.name.lower().replace(".csv", "")

    def setup_result_logging(self) -> None:
        if self.results_dir is None:
            self.results_dir = self.data_dir.joinpath("logs")
        else:
            self.results_dir = Path(self.results_dir).resolve()
        try:
            if not self.results_dir.is_dir():
                self.results_dir.mkdir(exist_ok=True, parents=False)
        except FileExistsError:
            raise FileExistsError(
                "Tried to create a directory for validation results at \n"
                f"  - {self.results_dir}\nbut there's already a file in that "
                "location. Please pass in a different\nlocation to the "
                "results_dir argument."
            )
        except PermissionError:
            raise PermissionError(
                "Tried to create a directory for validation results at \n"
                f"  - {self.results_dir}\nbut you do not have permission to "
                "write to that location. Please pass in a\ndifferent location"
                " to the results_dir argument."
            )
        except FileNotFoundError:
            raise FileNotFoundError(
                "Tried to create a directory for validation results at \n"
                f"  - {self.results_dir}\nbut there isn't a directory at\n"
                f"  - {self.results_dir.parent}\nIf that's the "
                "correct location you want to output results to, please "
                "create\neither directory and try again."
            )

    def set_data_format_to_path_map(self) -> None:
        self.data_format_to_path_map = {
            p.name.lower().replace(".csv", ""): p
            for p in self.data_dir.iterdir()
            if p.is_file()
            and p.name.lower().replace(".csv", "") in self.expected_data_formats
        }

    def check_for_missing_formats(self) -> None:
        missing_formats = [
            edf
            for edf in self.expected_data_formats
            if edf not in self.data_format_to_path_map.keys()
        ]
        if len(missing_formats) > 0:
            for missing_data_format in missing_formats:
                self.missing_data_formats.add(missing_data_format)
                self.issues.append(
                    {
                        "data_format": missing_data_format,
                        "issue_type": "missing_data_file",
                        "issue_details": {"data_dir": str(self.data_dir)},
                    }
                )

    def run_data_validations(self) -> None:
        for data_format, file_path in self.data_format_to_path_map.items():
            data_validator_cls = self.DATA_FORMAT_VALIDATORS.get(data_format)
            data_validator = data_validator_cls(file_path)
            # data_validator.file_validator.run_single_file_validations()
            print(f"Ran single-file validations for the {data_format} format.")
            new_issues = data_validator.file_validator.issues
            if len(new_issues) > 0:
                self.issues.extend(new_issues)
            self.DATA_FORMAT_VALIDATORS[data_format] = data_validator

        all_present_flag = len(self.data_format_to_path_map.keys()) == len(
            self.expected_data_formats
        )
        if all_present_flag:
            self.run_challenges_and_challengers_validations()
            self.run_cai_challenges_and_challengers_validations()
            print("TODO: add more multi-file validations here")

        self.output_results()

    def run_challenges_and_challengers_validations(self) -> None:
        challengers_in_challenges = list(
            set(
                el.lower()
                for el in self.DATA_FORMAT_VALIDATORS[
                    "challenges"
                ].file_validator.csv_data_object["challenger"]
            )
        )
        registered_challengers = list(
            set(
                el.lower()
                for el in self.DATA_FORMAT_VALIDATORS[
                    "challengers"
                ].file_validator.csv_data_object["challenger"]
            )
        )
        unregistered_yet_submitting_challengers = list(
            c
            for c in challengers_in_challenges
            if c not in registered_challengers
        )
        if len(unregistered_yet_submitting_challengers) > 0:
            self.issues.append(
                {
                    "data_format": "challenges",
                    "issue_type": "multi_file_validation",
                    "issue_details": {
                        "other_data_format": "challengers",
                        "message": (
                            "Found challengers in the Challenges dataset that"
                            " aren't in the Challengers dataset.\n"
                            "Unknown Challenger_ids in Challenges: "
                            f"{unregistered_yet_submitting_challengers}"
                        ),
                    },
                }
            )

    def run_cai_challenges_and_challengers_validations(self) -> None:
        challengers_in_cai_challenges = list(
            set(
                el.lower()
                for el in self.DATA_FORMAT_VALIDATORS[
                    "cai_challenges"
                ].file_validator.csv_data_object["challenger"]
            )
        )
        registered_challengers = list(
            set(
                el.lower()
                for el in self.DATA_FORMAT_VALIDATORS[
                    "challengers"
                ].file_validator.csv_data_object["challenger"]
            )
        )
        unregistered_yet_submitting_challengers = list(
            c
            for c in challengers_in_cai_challenges
            if c not in registered_challengers
        )
        if len(unregistered_yet_submitting_challengers) > 0:
            self.issues.append(
                {
                    "data_format": "cai_challenges",
                    "issue_type": "multi_file_validation",
                    "issue_details": {
                        "other_data_format": "challengers",
                        "message": (
                            "Found challengers in the CAIChallenges dataset"
                            " that aren't in the Challengers dataset.\n"
                            "Unknown Challenger_ids in CAIChallenges: "
                            f"{unregistered_yet_submitting_challengers}"
                        ),
                    },
                }
            )

    def output_results(self) -> None:
        if self.results_dir is None:
            print(self.issues)
        else:
            time_now = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_path = self.results_dir.joinpath(
                f"validation_issue_logs_{time_now}.json"
            )
            write_issues_to_json(issues=self.issues, file_path=log_path)
            print(f"Issues written to this file: {log_path}")
        print(
            f"Number of issues (or types of issues) found: {len(self.issues)}"
        )


def write_issues_to_json(issues: list[dict], file_path: Path) -> None:
    with open(file_path, "w") as json_file:
        json.dump(issues, json_file, indent=4)
