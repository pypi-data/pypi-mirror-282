import argparse
from pathlib import Path

from bread_inspektor.validator import BEADChallengeDataValidator


def main():
    parser = argparse.ArgumentParser(description="Validate NTIA Data.")
    parser.add_argument(
        "directory", type=str, help="The directory to check for the files."
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default="*",
        help="List of files (without .csv) to check for.",
    )
    parser.add_argument(
        "--results_dir",
        default=None,
        help="A dir to logs issues to (rather than printing to console).",
    )

    args = parser.parse_args()

    data_directory = Path(args.directory).resolve()
    BEADChallengeDataValidator(
        data_directory=data_directory,
        expected_data_formats=args.files,
        results_dir=args.results_dir,
    )


if __name__ == "__main__":
    main()
