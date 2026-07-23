import json
from pathlib import Path

config_path = Path(__file__).parent.parent / "config" / "config.json"

with open(config_path, "r") as file:
    config = json.load(file)

print(config)