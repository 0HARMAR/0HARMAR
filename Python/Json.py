import json

with open("Python/inscode.json",'r') as jsonfile:
    data = json.load(jsonfile)
print(type(data))

print(data)

for key,value in data.items():
    print(f"{type(key)} {key} : {type(value)} {value}")