from os import makedirs
from os.path import join

def touch( dir , name=None ):
    try:
        makedirs(dir)
    except OSError as e:
        print( f' os.makedirs("{ dir }") ERROR: { e.strerror }' )

    if(name):
        open( join( dir, name) , 'w').close()

#how to use 
#touch('only_Dir/onlyDir2/')
#touch('dirAndFile/dirAndFile2/','file.txt')
