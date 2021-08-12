from touch import touch
from jsonReader import jsonFileToData

index = int( input(' Which is the number of the exercise that you want to create? ' ) ) 
index = index -1

root     = '../../'
jsonFile = root + 'tools/data.json'
data = jsonFileToData( jsonFile )
exercise = data[index]

def title1(string):
    return f'# {string} { exercise["id"] }\n\n'
def description(string):
    return f'{string}\n\n'

def title2(string):
    return f'## {string}\n\n'

def listExamples(string):
    return f'{string}\n\n'

def title3(string):
    return f'## {string}\n\n'

def sectionNext(string):
    temp = ''
    if index > 0:
        number = data[ index-1 ]["id"]	
        temp = f'- [{string} {number}]({number})\n' 

    number = data[ index ]["id"]	
    temp += f'- **{string} {number}**\n' 

    number = data[ index + 1 ]["id"]	
    temp +=  f'- [{string} {number}]({number})\n' 

    return temp



def writeExerciseReadme(idiom,content):
    dirPath = root + idiom + '/' + exercise['id'] + '/'
    readmePath = dirPath + 'README.md'
    touch(dirPath)
    file = open( readmePath, 'w')
    file.write(content)
    file.close()

    print(f'Was wrrite on file {readmePath} :')
    print(content)

enReadme  = title1('Exercise')
enReadme += description(exercise['en'])
enReadme += title2('Examples')
enReadme += listExamples('No example yet')
enReadme += title3('Next')
enReadme += sectionNext('Exercise')

writeExerciseReadme('en',enReadme)


ptReadme  = title1('Exercício')
ptReadme += description(exercise['pt'])
ptReadme += title2('Exemplos')
ptReadme += listExamples('Nenhum exemplo ainda')
ptReadme += title3('Próximo')
ptReadme += sectionNext('Exercício')

writeExerciseReadme('pt',ptReadme)

