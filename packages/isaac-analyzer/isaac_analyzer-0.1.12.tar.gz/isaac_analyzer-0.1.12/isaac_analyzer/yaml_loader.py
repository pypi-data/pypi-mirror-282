import os
import yaml
from pkg_resources import resource_stream


def load_yaml(filename):
    """Load YAML file into a dictionary from the resource folder."""
    yaml_path = os.path.join("resources", filename)
    with open(yaml_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def load_yaml_full_path(file_path):
    """Load YAML file into a dictionary from a given path."""
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def load_yaml_resource(name):
    """Load YAML file into a dictionary from a resource name."""
    with resource_stream("isaac_analyzer", f"resources/{name}") as file:
        data = yaml.safe_load(file)
    return data
