from touch import touch
from jsonReader import jsonFileToData

#index = int( input(' Which is the number of the exercise that you want to create? ' ) )
index = 0

root     = '../../'
jsonFile = root + 'tools/data/data.json'
data = jsonFileToData( jsonFile )
#exercise = data[index]
exercise = None

def h1(string):
    return f'# {string}\n\n'

def h2(string):
    return f'## {string}\n\n'

def h3(string):
    return f'### {string}\n\n'

def listExamples():
    return f'- [python](python)\n\n'

def sectionNext(string, language=None):
    parentDir = '../'
    subDir = ''
    temp = ''
    if language:
        parentDir += '../'
        subDir = language

    if index > 0:
        number = data[ index-1 ]["number"]
        temp += f'- [{string} {number}]({parentDir + number + subDir})\n'

    number = data[ index ]["number"]
    temp += f'- **{string} {number}**\n'

    number = data[ index + 1 ]["number"]
    temp += f'- [{string} {number}]({parentDir + number + subDir})\n'
    temp += f'- [Lista de Exercicios]({parentDir})\n\n'
    return temp

def thumbnail(string):
    return f'[![{string}](https://img.youtube.com/vi/{exercise["videoId"]}/maxresdefault.jpg)](https://youtu.be/{exercise["videoId"]})'

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

def writeExerciseReadme():
    readme  = h1(exercise['pt'])
    readme += h2('Exemplo')
    readme += listExamples()
    readme += h2('Próximo')
    readme += sectionNext('Exercício')
    readme += h2('Video do exercício')
    readme += thumbnail('Video do exercício')
    writeFile(exerciseFolder('pt'), 'README.md', readme)

def writeExampleReadme():
    readme  = h1(exercise['pt'])
    readme += h2('Exemplo em Python')
    readme += h3('codigo')
    readme += "``` python\n[coloque o seu codigo aqui]\n```\n\n"
    readme += h3('saida')
    readme += "```\n[coloque a saida do seu codigo aqui]\n```\n\n"
    readme += h2('Próximo')
    readme += sectionNext('Exercício','python')
    writeFile(exampleFolder('pt','python'), 'README.md', readme)

def writeExampleCode():
    code  = h1(exercise['pt'])
    #code += "\n´´´ OUTPUT -->\n\n\n´´´"
    writeFile(exampleFolder('pt','python'), 'main.py', code)

def createAllData():
    global exercise
    global index
    for i, element in enumerate(data):
        exercise = element
        index = i
        writeExerciseReadme()
        writeExampleReadme()
        writeExampleCode()
        input('pausa')

createAllData()
