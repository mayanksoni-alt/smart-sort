import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.json"


def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path, "r") as file:
        data = json.load(file)

    # Normalize once here so every other module can just use the values
    # directly, instead of each doing its own path-expansion / type work.
    data["watch_folder"] = Path(data["watch_folder"]).expanduser()
    data["ignored_extensions"] = set(data.get("ignored_extensions", []))
    return data


config = load_config()