import argparse
import logging
import os
from isaac_analyzer import __version__
from isaac_analyzer.items import print_items
from isaac_analyzer.validator import validate_yaml

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        "file_path", type=str, help="Path to the YAML file to validate"
    )

    args = parser.parse_args()

    # Adjust log level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")
    else:
        logging.getLogger().setLevel(logging.INFO)

    if args.command == "items":
        if args.items_command == "print":
            print_items()
    elif args.command == "validate":
        validate_yaml(args.file_path, os.path.join("resources", "run_file_schema.json"))


if __name__ == "__main__":
    main()
