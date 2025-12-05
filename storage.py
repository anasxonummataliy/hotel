import json


def get_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)




def get_new_id(malumotlar: list[dict]):
    return max([m.get("id", 1) for m in malumotlar]) + 1