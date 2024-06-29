import datetime as dt
import re
from enum import Enum
from typing import Any, Callable, Optional, Protocol

# TODO: To make this more extensive we should put it in a file
# TODO: Valid vs. invalid tech codes.


class Validator(Protocol):
    @classmethod
    def validator(cls) -> Callable[Any, bool]:
        ...


class RuleValidator(Validator):
    @property
    def rule_descr(self) -> str:
        ...


class DjangoEnum(Enum):
    """Enum with a short and long name. Meant to be inherited."""

    def __new__(cls, short, long, *args):
        obj = object.__new__(cls)
        obj._value_ = short
        obj.short = short
        obj.long = long
        return obj

    @classmethod
    def get_choices(cls) -> list[tuple[str, str]]:
        return [(group.short, group.long) for group in cls]

    @classmethod
    def get_values(cls) -> list:
        return [type.value for type in cls]

    @classmethod
    def validator(cls):
        # Return a function which evaluates True/False
        # for a specific value.
        return lambda x: x in cls.get_values()


class ValidatorEnum(Enum):
    @classmethod
    def get_choices(cls) -> list[tuple[str, str]]:
        return [(group.short, group.long) for group in cls]

    @classmethod
    def get_values(cls) -> list:
        return [type.name for type in cls]

    @classmethod
    def validator(cls):
        # Return a function which evaluates True/False
        # for a specific value.
        return lambda x: x in cls.get_values()


class PhoneValidator:
    @classmethod
    def validator(cls):
        return (
            lambda x: x is None
            or x == ""
            or bool(re.match(r"^\d{3}-\d{3}-\d{4}$", x))
        )


class ZipNullableValidator:
    @classmethod
    def validator(cls):
        return (
            lambda x: x == "" or x is None or bool(re.match(r"^\d{5}$", str(x)))
        )


class ChallengeIdValidator:
    @classmethod
    def validator(cls):
        return lambda x: len(x) <= 50 and bool(re.match(r"^[A-Za-z0-9-]+$", x))


class DateValidator:
    @classmethod
    def validator(cls) -> Callable[[Optional[str]], bool]:
        def validate(x: Optional[str]) -> bool:
            try:
                dt.datetime.strptime(x, "%Y-%m-%d")
                return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", x))
            except ValueError:
                return False

        return validate


class DateNullableValidator:
    @classmethod
    def validator(cls) -> Callable[[Optional[str]], bool]:
        def validate(x: Optional[str] = None) -> bool:
            try:
                if x == "" or x is None:
                    return True
                dt.datetime.strptime(x, "%Y-%m-%d")
                return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", x))
            except ValueError:
                return False

        return validate


class EmailValidator:
    @classmethod
    def validator(cls):
        # RegEx to validate an email address with a single '@' sign
        return lambda x: bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", x))


class FileNameValidator:
    @classmethod
    def validator(cls) -> Callable[[str], bool]:
        def validate(file_name: str) -> bool:
            return bool(
                re.match(r"^[A-Za-z0-9_\-/\\]+\.pdf$", file_name, re.IGNORECASE)
            )

        return validate


class FileNameNullableValidator:
    @classmethod
    def validator(cls) -> Callable[[str], bool]:
        def validate(file_name: Optional[str] = None) -> bool:
            if file_name == "" or file_name is None:
                return True
            return bool(
                re.match(r"^[A-Za-z0-9_\-/\\]+\.pdf$", file_name, re.IGNORECASE)
            )

        return validate


class LatitudeNullableValidator:
    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x is None or x == "":
            return True
        try:
            return -90.0 <= float(x) <= 90.0
        except ValueError:
            return False


class LongitudeNullableValidator:
    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x is None or x == "":
            return True
        try:
            return -180.0 <= float(x) <= 180.0
        except ValueError:
            return False


class BSLLocationIdValidator:
    # Per the page at the URL:
    #     "Each Location ID is a 10-digit number starting with one billion."
    # (
    #     "https://help.bdc.fcc.gov/hc/en-us/articles/5291539645339-How-to-"
    #     "Format-Fixed-Broadband-Availability-Location-Lists"
    # )
    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x is None or x == "":
            return False
        try:
            return 10**9 <= int(x) < 10**10
        except ValueError:
            return False


class BSLLocationIdNullableValidator:
    # Per the page at the URL:
    #     "Each Location ID is a 10-digit number starting with one billion."
    # (
    #     "https://help.bdc.fcc.gov/hc/en-us/articles/5291539645339-How-to-"
    #     "Format-Fixed-Broadband-Availability-Location-Lists"
    # )

    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x is None or x == "":
            return True
        try:
            return 10**9 <= int(x) < 10**10
        except ValueError:
            return False


class WebPageValidator:
    @classmethod
    def validator(cls):
        # RegEx to check if the URL starts with http:// or https://
        return (
            lambda x: x == ""
            or x is None
            or bool(re.match(r"^(http://|https://)", x))
        )


class NonNegativeNumberValidator:
    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x == "" or x is None:
            return False
        try:
            return float(x) >= 0
        except ValueError:
            return False


class NonNegativeNumberNullableValidator:
    @classmethod
    def validator(cls):
        return lambda x: cls._validate(x)

    @staticmethod
    def _validate(x):
        if x == "" or x is None:
            return True
        try:
            return float(x) >= 0
        except ValueError:
            return False


class NonNullableValidator:
    @classmethod
    def validator(cls) -> Callable[[str], bool]:
        return lambda x: x != "" and x is not None


class FccProviderIdValidator:
    @classmethod
    def validator(cls):
        # RegEx to check if the string is a 6-digit number
        return (
            lambda x: x == ""
            or x is None
            or bool(re.match(r"^[1-9]\d{5}$", str(x)))
        )


class CAIRationale(ValidatorEnum):
    """Contains CAI Rationale category codes"""

    X = "CAI has ceased operation"
    B = "Location does not require broadband service"
    R = "CAI is a private residence or non-CAI business"
    D = (
        "Definition: The challenger believes that this either fails"
        " to meet or meets the definition"
    )
    N = "New CAI"
    I = "Independent location"  # noqa E741
    T = "The CAI Type is incorrect"
    O = "Other, as described in the explanation column"  # noqa E741


class CAIRationaleNullableValidator:
    Rationale = CAIRationale

    @classmethod
    def validator(cls):
        return (
            lambda x: x == ""
            or x is None
            or x in [r.name for r in cls.Rationale]
        )


class CMSCertificateNullableValidator:
    @classmethod
    def validator(cls):
        pattern = r"^[a-zA-Z0-9]{6}$|^[a-zA-Z0-9]{10}$"
        return (
            lambda x: x == ""
            or x is None
            or (len(str(x)) <= 10 and bool(re.match(pattern, str(x))))
        )


class FrnNullableValidator:
    @classmethod
    def validator(cls):
        pattern = r"^\d{10}$"
        return lambda x: x == "" or x is None or bool(re.match(pattern, str(x)))


class TechCode(ValidatorEnum):
    """Contains technology codes

    In the tuple below the data structure is:
        NTIA Technology Code
        Technology Name

    The methods below return the information.
    """

    _10 = (10, "Copper Wire")
    _40 = (40, "Coaxial Cable")
    _50 = (50, "Optical Carrier / Fiber to the Premises")
    _60 = (60, "Geostationary Satellite")
    _61 = (61, "Non-Geostationary Satellite")
    _70 = (70, "Unlicensed Terrestrial Fixed Wireless")
    _71 = (71, "Licensed Terrestrial Fixed Wireless")
    _72 = (72, "Licensed-by-Rule Terrestrial Fixed Wireless")
    _0 = (0, "Other")

    def __new__(cls, tech_code, tech_description):
        obj = object.__new__(cls)
        obj._value_ = (tech_code, tech_description)
        obj.tech_code = tech_code
        obj.tech_description = tech_description
        return obj

    @classmethod
    def get_values(cls) -> list:
        return [tech.tech_code for tech in cls]

    @classmethod
    def get_choices(cls) -> list[tuple[str, str]]:
        return [
            (group.tech_code, f"{group.tech_description} ({group.tech_code})")
            for group in cls
        ]

    @classmethod
    def validator(cls):
        return lambda x: x == "" or x is None or x in cls.get_values()


class PlannedOrExistingChoices(ValidatorEnum):
    P = "Planned"
    E = "Existing"

    @classmethod
    def get_choices(cls):
        return [(type.name, type.value) for type in cls]


class EnforceableCommitments(Enum):
    _1 = "Connect America Fund Phase II (CAFII)"
    _2 = "Enhanced Alternative Connect America Cost Model (EACAM)"
    _3 = "Rural Digital Opportunity Fund (RDOF)"
    _4 = "Broadband Infrastructure Program (BIP)"
    _5 = "USDA Community Connect Grant Program (CCG)"
    _6 = "USDA ReConnect Program (RCP)"
    _7 = "Telephone Loan Program (TLP)"
    _8 = "Connect Illinois Round 1 (CI1)"
    _9 = "Connect Illinois Round 2 (CI2)"
    _10 = "Connect Illinois Round 3 (CI3)"
    _11 = "American Rescue Plan Act - Other Local Funding (ARPA)"
    _12 = "Other State Funding Program (OS)"
    _13 = "Other Federal Funding Program (OF)"

    @classmethod
    def get_choices(cls):
        return [int(member.value) for member in cls]


class CAICategoryCode(Enum):
    I = (  # noqa E741
        "I: CAI affiliated with a listed CAI, at a separate "
        "location requiring broadband service (For C challenge types only)"
    )
    N = (
        "N: CAI established or operational by June 30, 2024 "
        "(For C challenge types only)"
    )
    T = "T: CAI type is wrong (For C challenge types only)"
    D = (
        "D: Location either is a CAI (challenge type C) or isn't a CAI "
        "(challenge type R) (For C or R challenge types)"
    )
    O = "O: Other; describe in Explanation (For C or R challenge types)"  # noqa E741
    B = "B: CAI has ceased operation (For R challenge types only)"
    R = (
        "R: CAI is a private residence or a non-CAI business "
        "(For R challenge types only)"
    )
    X = (
        "X: Location does not require fiber broadband service appropriate "
        "for CAI (For R challenge types only)"
    )

    @classmethod
    def get_valid_C_choices(cls):
        return [
            (type.name, type.value)
            for type in cls
            if type.name in cls.get_valid_C_values(cls)
        ]

    @classmethod
    def get_valid_R_choices(cls):
        return [
            (type.name, type.value)
            for type in cls
            if type.name in cls.get_valid_R_values(cls)
        ]

    @classmethod
    def get_valid_C_values(cls):
        return ["I", "N", "T", "D", "O"]

    @classmethod
    def get_valid_R_values(cls):
        return ["D", "O", "B", "R", "X"]

    @classmethod
    def get_choices(cls):
        return [(type.name, type.value) for type in cls]

    @classmethod
    def get_values(cls):
        return [type.name for type in cls]


class ChallengerType(ValidatorEnum):
    L = "Unit of Local Government"
    T = "A Tribal Government"
    N = "Nonprofit Org"
    B = "Broadband Provider"


class State(ValidatorEnum):
    AL = "Alabama"
    AK = "Alaska"
    AS = "American Samoa"
    AZ = "Arizona"
    AR = "Arkansas"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    DC = "District of Columbia"
    FL = "Florida"
    GA = "Georgia"
    GU = "Guam"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MD = "Maryland"
    MA = "Massachusetts"
    MI = "Michigan"
    MN = "Minnesota"
    MS = "Mississippi"
    MO = "Missouri"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    MP = "Northern Mariana Islands"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PA = "Pennsylvania"
    PR = "Puerto Rico"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    VI = "U.S. Virgin Islands"
    UT = "Utah"
    VT = "Vermont"
    VA = "Virginia"
    WA = "Washington"
    WV = "West Virginia"
    WI = "Wisconsin"
    WY = "Wyoming"


class CAIType(ValidatorEnum):
    S = "S: School or institute of higher education"
    L = "L: Library"
    G = "G: Government building"
    H = (
        "H: Health clinic, health center, hospital,"
        " or another medical provider"
    )
    F = "F: Public safety entity"
    P = "P: Public housing organization"
    C = "C: Community support organization"
    K = "K: Park"

    @classmethod
    def get_choices(cls):
        return [(type.name, type.value) for type in cls]


class ChallengeType(ValidatorEnum):
    A = "Availability (A)"
    S = "Speed (S)"
    L = "Latency (L)"
    D = "Data Cap (D)"
    T = "Technology (T)"
    B = "Business Service Only (B)"
    P = "Planned (or Existing) Service (P)"
    E = "Enforceable Commitment (E)"
    N = "Not Part of Enforceable Commitment (N)"
    # C = "Location is a CAI (C)"
    # R = "Location is NOT a CAI (R)"
    # G = "CAI cannot obtain qualifying broadband (G)"
    # Q = "CAI can obtain qualifying broadband (Q)"
    V = "Pre-challenge mod for DSL technology (V)"
    F = "Pre-challenge mod for fixed wireless technology (F)"
    M = "Pre-challenge mod for measurement-based anonymous speed tests (M)"
    X = "NTIA-approved eligible entity pre-challenge mod 1 (X)"
    Y = "NTIA-approved eligible entity pre-challenge mod 2 (Y)"
    Z = "NTIA-approved eligible entity pre-challenge mod 3 (Z)"

    @classmethod
    def get_choices(cls):
        return [(type.name, type.value) for type in cls]


class CAIChallengeType(ValidatorEnum):
    C = "Location is a CAI (C)"
    R = "Location is NOT a CAI (R)"
    G = "CAI cannot obtain qualifying broadband (G)"
    Q = "CAI can obtain qualifying broadband (Q)"

    @classmethod
    def get_choices(cls):
        return [(type.name, type.value) for type in cls]


class Submitter(Enum):
    CAI = "CAI"
    ISP = "ISP"
    GOV = "Government Organization"
    IND = "Individual"

    @classmethod
    def get_choices(cls):
        return [(submitter.name, submitter.value) for submitter in cls]


class DispositionsOfChallenge(ValidatorEnum):
    I = "Incomplete"  # noqa
    N = "No rebuttal"
    A = "Provider agreed"
    S = "Sustained after rebuttal"
    R = "Rejected after rebuttal"
    M = "Moot due to another successful challenge"

    @classmethod
    def get_choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class DispositionsOfCAIChallenge(ValidatorEnum):
    I = "Incomplete"  # noqa
    N = "No rebuttal"
    A = "Provider agreed"
    S = "Sustained after rebuttal"
    R = "Rejected after rebuttal"

    @classmethod
    def get_choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class ResidentialOrBusiness(ValidatorEnum):
    R = ("R", "Residential")
    B = ("B", "Business")

    @classmethod
    def get_choices(cls):
        return [(member.value[0], member.value[1]) for member in cls]


class ReasonCode(DjangoEnum):
    _1 = (
        "1",
        (
            "Provider failed to schedule a service installation "
            "within 10 business days of a request (1)."
        ),
    )
    _2 = (
        "2",
        "Provider did not install the service at the agreed-upon time (2).",
    )
    _3 = (
        "3",
        (
            "Provider requested more than the standard installation fee "
            "to connect the location (3)."
        ),
    )
    _4 = ("4", "Provider denied the request for service (4).")
    _5 = (
        "5",
        (
            "Provider does not offer the technology entered "
            "above at this location (5)."
        ),
    )
    _6 = (
        "6",
        (
            "Provider does not offer the speed(s) shown on the Broadband Map "
            "for purchase at this location (6)."
        ),
    )
    _8 = (
        "8",
        (
            "No wireless signal is available at this location "
            "(only for technology codes 70 and above) (8)."
        ),
    )
    _9 = (
        "9",
        (
            "New, non-standard equipment had to be constructed "
            "at this location (9)."
        ),
    )

    @classmethod
    def get_codes(cls):
        return [int(member.value[0]) for member in cls]

    @classmethod
    def validator(cls):
        # Return a function which evaluates True/False
        # for a specific value.
        return lambda x: x in cls.get_values() or x == "" or x is None


class LocationClassificationCode(ValidatorEnum):
    _0 = ("0", "Unserved")
    _1 = ("1", "Underserved")
    _2 = ("2", "Served")

    @classmethod
    def get_choices(cls):
        return [int(member.value[0]) for member in cls]

    @classmethod
    def validator(cls):
        return lambda x: x in cls.get_choices()
