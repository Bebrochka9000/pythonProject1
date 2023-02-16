import json


def load_condidates():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
