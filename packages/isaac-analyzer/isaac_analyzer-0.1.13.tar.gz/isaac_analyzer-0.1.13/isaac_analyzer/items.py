import logging
from tabulate import tabulate
from isaac_analyzer.yaml_loader import load_yaml_resource

logger = logging.getLogger(__name__)


def print_items():
    """Print items from items.yaml."""
    data = load_yaml_resource("items.yaml")
    logger.debug("Printing all items from items.yaml")
    items = data.get("items", [])
    if isinstance(items, list) and all(isinstance(item, dict) for item in items):
        table = tabulate(items, headers="keys", tablefmt="github")
        print(table)
