import json

file = open('../data.json')

data = json.load(file)

file.close()

for object in data:
    print(object['id'])

