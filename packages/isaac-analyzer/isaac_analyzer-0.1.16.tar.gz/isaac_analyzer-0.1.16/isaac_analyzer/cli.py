import argparse
import os
from isaac_analyzer import __version__
from isaac_analyzer.items import print_items
from isaac_analyzer.validator import validate_yaml
from isaac_analyzer.logging import init, getLogger
from glob import glob
from logging import DEBUG, INFO

logger = getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="isaac-analyzer: A CLI application to analyze isaac runs"
    )
    parser.add_argument(
        "--version", action="version", version=f"isaac-analyzer {__version__}"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Sub-parser for 'items print' command
    parser_items = subparsers.add_parser(
        "items", help="Operations related to items.yaml"
    )
    parser_items_subparsers = parser_items.add_subparsers(
        dest="items_command", help="Items command help"
    )

    parser_items_subparsers.add_parser("print", help="Print items from items.yaml")

    parser_validate = subparsers.add_parser(
        "validate", help="Validate a YAML file against the schema"
    )
    parser_validate.add_argument(
        "-f", "--file", type=str, help="Path to a single YAML file to validate"
    )
    parser_validate.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Path to a directory containing YAML files to validate",
    )

    args = parser.parse_args()

    # Adjust log level based on verbose flag
    if args.verbose:
        init(DEBUG)
        logger.debug("Verbose logging enabled.")
    else:
        init(INFO)

    if args.command == "items":
        if args.items_command == "print":
            print_items()
    elif args.command == "validate":
        if args.file:
            validate_single_file(args.file)
        elif args.directory:
            validate_directory(args.directory)
        else:
            logger.error("Please specify either -f or -d option.")
            parser.print_help()


def validate_single_file(file_path):
    schema_path = os.path.join("resources", "run_file_schema.json")
    try:
        validate_yaml(file_path, schema_path)
    except Exception as e:
        logger.debug(f"{e}")


def validate_directory(directory_path):
    schema_path = os.path.join("resources", "run_file_schema.json")
    yaml_files = glob(os.path.join(directory_path, "*.y*ml"))
    all_valid = True

    for yaml_file in yaml_files:
        try:
            validate_yaml(yaml_file, schema_path)
        except Exception:
            all_valid = False
            logger.error(f"Validation failed for file: {yaml_file}")

    if all_valid:
        logger.info("All YAML files are valid.")
    else:
        logger.error("Some YAML files failed validation. See error messages above.")


if __name__ == "__main__":
    main()
