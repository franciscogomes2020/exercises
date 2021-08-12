import json

def jsonFileToData(path):
    file = open(path)
    data = json.load(file)
    file.close()
    return data

# how to use
# data = jsonFileToData('../data.json')
# print( data )
