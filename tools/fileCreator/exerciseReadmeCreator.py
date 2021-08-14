from touch import touch
from jsonReader import jsonFileToData

index = int( input(' Which is the number of the exercise that you want to create? ' ) ) 
index = index -1

root     = '../../'
jsonFile = root + 'tools/data/data.json'
data = jsonFileToData( jsonFile )
exercise = data[index]

def title1(string):
    return f'# {string}\n\n'

def title2(string):
    return f'## {string}\n\n'

def listExamples(string):
    return f'{string}\n\n'

def title3(string):
    return f'## {string}\n\n'

def sectionNext(string):
    temp = ''
    if index > 0:
        number = data[ index-1 ]["number"]	
        temp = f'- [{string} {number}](../{number})\n'

    number = data[ index ]["number"]	
    temp += f'- **{string} {number}**\n' 

    number = data[ index + 1 ]["number"]	
    temp +=  f'- [{string} {number}](../{number})\n'

    return temp

def linkToExerciseList(string):
    return f'- [{string}](..)\n\n' 

def thumbnail(string):
    return f'[![{string}](https://img.youtube.com/vi/{exercise["videoId"]}/maxresdefault.jpg)](https://youtu.be/{exercise["videoId"]})'

def writeExerciseReadme(idiom,content):
    dirPath = root + idiom + '/' + exercise["number"] + '/'
    readmePath = dirPath + 'README.md'
    touch(dirPath)
    file = open( readmePath, 'w')
    file.write(content)
    file.close()

    print(f'Was wrrite on file {readmePath} :')
    print(content)

ptReadme  = title1(exercise['pt'])
ptReadme += title2('Exemplos')
ptReadme += listExamples('Nenhum exemplo ainda')
ptReadme += title3('Próximo')
ptReadme += sectionNext('Exercício')
ptReadme += linkToExerciseList('Lista de Exercícios')
ptReadme += title2('Video do [@gustavoguanabara](https://github.com/gustavoguanabara) desse exercício')
ptReadme += thumbnail('Video do exercício')

writeExerciseReadme('pt',ptReadme)
