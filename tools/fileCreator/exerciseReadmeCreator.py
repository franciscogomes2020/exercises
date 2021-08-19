from touch import touch
from jsonReader import jsonFileToData
import re

root     = '../../'
jsonFile = root + 'tools/data/data.json'
data = jsonFileToData( jsonFile )
exercise = None
index = 0

def exerciseFolder(idiom):
    return root + idiom + '/' + exercise["number"] + '/'

def exampleFolder(idiom, language):
    return exerciseFolder(idiom) + language + '/'

def writeFile(dir,name,content):
    touch(dir)
    with open( dir + name, 'w', encoding='utf-8') as file:
        file.write(content)
        file.close()
    hr = f'\n{60 * "-"}\n'
    print(f'{hr}{dir + name} was wrote it:{hr}{content}{hr}')

def createAllData():
    global index
    for i, element in enumerate(data):
        index = i
        createFiles()

def getFileContent(path):
    with open(path) as file:
        content = file.read()
        file.close()
        return content

TEMPLATE_EXERCISE_README = getFileContent(root + 'tools/template/en/000/README.md')
TEMPLATE_EXAMPLE_README = getFileContent(root + 'tools/template/en/000/python/README.md')
TEMPLATE_EXAMPLE_MAIN = getFileContent(root + 'tools/template/en/000/python/main.py')

def removeLineWhichContet(content,string):
    return re.sub('\n.*' + content + '.*\n', '\n', string)

def createFiles():
    global exercise
    exercise = data[index]
    EXERCISE = data[index]['en']
    VIDEO_ID = data[index]['videoId']
    NUMBER   = data[index]['number']
    NUMBER_SUB_ONE  = ''
    NUMBER_PLUS_ONE = ''
    if index == 0:
        exerciseText = removeLineWhichContet('NUMBER_SUB_ONE',TEMPLATE_EXERCISE_README)
        exampleText  = removeLineWhichContet('NUMBER_SUB_ONE',TEMPLATE_EXAMPLE_README )
        NUMBER_PLUS_ONE = data[index+1]['number']
    elif index == len(data)-1:
        exerciseText = removeLineWhichContet('NUMBER_PLUS_ONE',TEMPLATE_EXERCISE_README)
        exampleText  = removeLineWhichContet('NUMBER_PLUS_ONE',TEMPLATE_EXAMPLE_README )
        NUMBER_SUB_ONE = data[index-1]['number']
    else:
        exerciseText = TEMPLATE_EXERCISE_README
        exampleText  = TEMPLATE_EXAMPLE_README
        NUMBER_SUB_ONE = data[index-1]['number']
        NUMBER_PLUS_ONE = data[index+1]['number']

    exerciseText = exerciseText .replace('EXERCISE',EXERCISE) .replace('NUMBER_PLUS_ONE',NUMBER_PLUS_ONE) .replace('NUMBER_SUB_ONE',NUMBER_SUB_ONE) .replace('NUMBER',NUMBER) .replace('VIDEO_ID',VIDEO_ID)
    exampleText  = exampleText  .replace('EXERCISE',EXERCISE) .replace('NUMBER_PLUS_ONE',NUMBER_PLUS_ONE) .replace('NUMBER_SUB_ONE',NUMBER_SUB_ONE) .replace('NUMBER',NUMBER) .replace('VIDEO_ID',VIDEO_ID)
    mainText     = TEMPLATE_EXAMPLE_MAIN     .replace('EXERCISE',EXERCISE)

    writeFile(exerciseFolder('en'), 'README.md', exerciseText)
    writeFile(exampleFolder('en','python'), 'README.md', exampleText)
    writeFile(exampleFolder('en','python'), 'main.py', mainText)

answer = input('Do you want to create all Data files? (y,n) ')
if answer == 'y':
    createAllData()
else:
    answer = input('betwen 1 and {} which exercise files do you want to create/override? (q to exit) '.format(len(data)))
    if answer.isnumeric():
        index = int(answer) -1
        createFiles()
    else:
        print('It is not a valid number')

print('Exiting of the program')
