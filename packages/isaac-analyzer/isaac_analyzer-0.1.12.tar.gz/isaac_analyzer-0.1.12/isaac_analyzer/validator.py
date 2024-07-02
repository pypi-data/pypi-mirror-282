import logging
from isaac_analyzer.yaml_loader import load_yaml_full_path
import json
import jsonschema
from jsonschema import Draft202012Validator
from pkg_resources import resource_stream

logger = logging.getLogger(__name__)


def load_schema(schema_path):
    logger.debug(f"Loading schema at: {schema_path}")
    with resource_stream("isaac_analyzer", schema_path) as file:
        return json.load(file)


def validate_yaml(file_path, schema_path):
    logger.info(f"Validating {file_path}")
    schema = load_schema(schema_path)
    logger.debug("Schema loaded")

    data = load_yaml_full_path(file_path)
    logger.debug("Yaml file loaded.")
    validator = Draft202012Validator(schema)

    try:
        validator.validate(data)
        logger.info("YAML file is valid.")
    except jsonschema.exceptions.ValidationError:
        for error in sorted(validator.iter_errors(data), key=str):
            logger.error(error)
