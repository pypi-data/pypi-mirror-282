import logging
from isaac_analyzer.yaml_loader import load_yaml_full_path
import json
import jsonschema
from jsonschema import validate

logger = logging.getLogger(__name__)


def load_schema(schema_path):
    logger.debug(f"Loading schema at: {schema_path}")
    with open(schema_path, "r") as file:
        return json.load(file)


def validate_yaml(file_path, schema_path):
    schema = load_schema(schema_path)
    logger.debug("Schema loaded")

    data = load_yaml_full_path(file_path)
    logger.debug("Yaml file loaded.")

    try:
        validate(instance=data, schema=schema)
        logger.info("YAML file is valid.")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"YAML file is invalid: {err.message}")
        logger.error(f"Failed validating {err.instance} at {list(err.path)}")
