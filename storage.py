import json


<<<<<<< HEAD
def get_data(fayl):
    try:
        with open(fayl, "r") as f:
=======
def get_data(file):
    try:
        with open(file, "r") as f:
>>>>>>> origin/main
            return json.load(f)
    except:
        return []


def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


<<<<<<< HEAD
def get_new_id(malumotlar):
    if not malumotlar:
        return 1
    return max([m.get("id", 0) for m in malumotlar]) + 1
=======


def get_new_id(malumotlar: list[dict]):
    return max([m.get("id", 1) for m in malumotlar]) + 1
>>>>>>> origin/main
