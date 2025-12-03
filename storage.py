import json


def get_data(fayl):
    try:
        with open(fayl, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def get_new_id(malumotlar):
    if not malumotlar:
        return 1
    return max([m.get("id", 0) for m in malumotlar]) + 1
