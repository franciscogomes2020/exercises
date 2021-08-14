import json 

def jsonFileToData(path):
    file = open(path, encoding='utf8')
    data = json.load(file)
    file.close()
    return data


def dataJsonMap(item):
    description = item['snippet']['description']
    number = description.split(':')[0]
    question = description.split('\n\n')[0]
    try:
        question = question.split(': ')[1]
    except:
        print(question)
    try:
        number = number.split('ython ')[1] 
    except: 
        print(number)
    return {
        'number'      : number,
        'videoId'     : item['snippet']['resourceId']['videoId'],
        'description' : description,
        'pt'          : question
        }


data  = jsonFileToData('playlist-page1.json')['items']
data += jsonFileToData('playlist-page2.json')['items']
data += jsonFileToData('playlist-page3.json')['items']

data = list(map(dataJsonMap, data))

with open('data.json','w') as outfile:
    json.dump(data, outfile, indent=1, ensure_ascii=False)
