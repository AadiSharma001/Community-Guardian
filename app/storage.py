import json
from pathlib import Path

DATA_FILE = Path("data/incidents.json")

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_next_id(data):
    return max([item["id"] for item in data], default=0) + 1