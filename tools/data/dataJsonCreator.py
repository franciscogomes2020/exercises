import json 

def jsonFileToData(path):
    file = open(path, encoding='utf8')
    data = json.load(file)
    file.close()
    return data


def dataJsonMap(item):
    return {
        'videoId'     : item['snippet']['resourceId']['videoId'],
        'description' : item['snippet']['description']
        }


data  = jsonFileToData('playlist-page1.json')['items']
data += jsonFileToData('playlist-page2.json')['items']
data += jsonFileToData('playlist-page3.json')['items']

data = list(map(dataJsonMap, data))

with open('data.json','w') as outfile:
    json.dump(data, outfile, indent=1, ensure_ascii=False)

