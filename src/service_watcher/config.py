import yaml
from pathlib import Path

CONFIG_FILE = Path("config/services.yaml")


def load_services() -> list[dict[str, str]]:
    with CONFIG_FILE.open(encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config["services"]