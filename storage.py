import json
import os


def get_data(file):
    try:
        if not os.path.exists(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_data(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_new_id(malumotlar: list[dict]):
    if not malumotlar:
        return 1
    return max([m.get("id", 0) for m in malumotlar]) + 1
