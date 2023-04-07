import json

data = {
    "president": {
        "name": "Бобёр",
        "country": "Forest Lake"
    }
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

with open("data.json", "r", encoding="utf-8") as file:
    load_data = json.load(file)

print(load_data)
