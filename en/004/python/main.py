# Make a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen 

userInput = input('\nType anything, I will show you info about it:\n')
print()

functionMask = '{:<' + str(15 + 3 + len(userInput) ) + '}= {}'
methodMask   = '"{}".{:<' + str(15) + '}= {}'

print( functionMask.format('type("{}")'.format(userInput), type(userInput) ) )  #show <class 'str'>
print( functionMask.format('len("{}")'.format(userInput),  len(userInput) ) )   #show length of the string

# https://www.w3schools.com/python/python_ref_string.asp

print( methodMask.format(userInput,'capitalize()',userInput.capitalize()) )     #Converts the first character to upper case
print( methodMask.format(userInput,'casefold()',userInput.casefold()) )         #Converts string into lower case
#print( methodMask.format(userInput,'center()',userInput.center()) )            #Returns a centered string
#print( methodMask.format(userInput,'count()',userInput.count()) )              #Returns the number of times a specified value occurs in a string
print( methodMask.format(userInput,'encode()',userInput.encode()) )             #Returns an encoded version of the string
#print( methodMask.format(userInput,'endswith()',userInput.endswith()) )        #Returns true if the string ends with the specified value
print( methodMask.format(userInput,'expandtabs()',userInput.expandtabs()) )     #Sets the tab size of the string
#print( methodMask.format(userInput,'find()',userInput.find()) )                #Searches the string for a specified value and returns the position of where it was found
print( methodMask.format(userInput,'format()',userInput.format()) )             #Formats specified values in a string
#print( methodMask.format(userInput,'format_map()',userInput.format_map()) )    #Formats specified values in a string
#print( methodMask.format(userInput,'index()',userInput.index()) )              #Searches the string for a specified value and returns the position of where it was found
print( methodMask.format(userInput,'isalnum()',userInput.isalnum()) )           #Returns True if all characters in the string are alphanumeric
print( methodMask.format(userInput,'isalpha()',userInput.isalpha()) )           #Returns True if all characters in the string are in the alphabet
print( methodMask.format(userInput,'isdecimal()',userInput.isdecimal()) )       #Returns True if all characters in the string are decimals
print( methodMask.format(userInput,'isdigit()',userInput.isdigit()) )           #Returns True if all characters in the string are digits
print( methodMask.format(userInput,'isidentifier()',userInput.isidentifier()) ) #Returns True if the string is an identifier
print( methodMask.format(userInput,'islower()',userInput.islower()) )           #Returns True if all characters in the string are lower case
print( methodMask.format(userInput,'isnumeric()',userInput.isnumeric()) )       #Returns True if all characters in the string are numeric
print( methodMask.format(userInput,'isprintable()',userInput.isprintable()) )   #Returns True if all characters in the string are printable
print( methodMask.format(userInput,'isspace()',userInput.isspace()) )           #Returns True if all characters in the string are whitespaces
print( methodMask.format(userInput,'istitle()',userInput.istitle()) )           #Returns True if the string follows the rules of a title
print( methodMask.format(userInput,'isupper()',userInput.isupper()) )           #Returns True if all characters in the string are upper case
#print( methodMask.format(userInput,'join()',userInput.join()) )                #Joins the elements of an iterable to the end of the string
#print( methodMask.format(userInput,'ljust()',userInput.ljust()) )              #Returns a left justified version of the string
print( methodMask.format(userInput,'lower()',userInput.lower()) )               #Converts a string into lower case
print( methodMask.format(userInput,'lstrip()',userInput.lstrip()) )             #Returns a left trim version of the string
#print( methodMask.format(userInput,'maketrans()',userInput.maketrans()) )      #Returns a translation table to be used in translations
#print( methodMask.format(userInput,'partition()',userInput.partition()) )      #Returns a tuple where the string is parted into three parts
#print( methodMask.format(userInput,'replace()',userInput.replace()) )          #Returns a string where a specified value is replaced with a specified value
#print( methodMask.format(userInput,'rfind()',userInput.rfind()) )              #Searches the string for a specified value and returns the last position of where it was found
#print( methodMask.format(userInput,'rindex()',userInput.rindex()) )            #Searches the string for a specified value and returns the last position of where it was found
#print( methodMask.format(userInput,'rjust()',userInput.rjust()) )              #Returns a right justified version of the string
#print( methodMask.format(userInput,'rpartition()',userInput.rpartition()) )    #Returns a tuple where the string is parted into three parts
print( methodMask.format(userInput,'rsplit()',userInput.rsplit()) )             #Splits the string at the specified separator, and returns a list
print( methodMask.format(userInput,'rstrip()',userInput.rstrip()) )             #Returns a right trim version of the string
print( methodMask.format(userInput,'split()',userInput.split()) )               #Splits the string at the specified separator, and returns a list
print( methodMask.format(userInput,'splitlines()',userInput.splitlines()) )     #Splits the string at line breaks and returns a list
#print( methodMask.format(userInput,'startswith()',userInput.startswith()) )    #Returns true if the string starts with the specified value
print( methodMask.format(userInput,'strip()',userInput.strip()) )               #Returns a trimmed version of the string
print( methodMask.format(userInput,'swapcase()',userInput.swapcase()) )         #Swaps cases, lower case becomes upper case and vice versa
print( methodMask.format(userInput,'title()',userInput.title()) )               #Converts the first character of each word to upper case
#print( methodMask.format(userInput,'translate()',userInput.translate()) )      #Returns a translated string
print( methodMask.format(userInput,'upper()',userInput.upper()) )               #Converts a string into upper case
#print( methodMask.format(userInput,'zfill()',userInput.zfill()) )              #Fills the string with a specified number of 0 values at the beginning


# OUTPUT -->
#
# Type anything, I will show you info about it:
# test
# 
# type("test")          = <class 'str'>
# len("test")           = 4
# "test".capitalize()   = Test
# "test".casefold()     = test
# "test".encode()       = b'test'
# "test".expandtabs()   = test
# "test".format()       = test
# "test".isalnum()      = True
# "test".isalpha()      = True
# "test".isdecimal()    = False
# "test".isdigit()      = False
# "test".isidentifier() = True
# "test".islower()      = True
# "test".isnumeric()    = False
# "test".isprintable()  = True
# "test".isspace()      = False
# "test".istitle()      = False
# "test".isupper()      = False
# "test".lower()        = test
# "test".lstrip()       = test
# "test".rsplit()       = ['test']
# "test".rstrip()       = test
# "test".split()        = ['test']
# "test".splitlines()   = ['test']
# "test".strip()        = test
# "test".swapcase()     = TEST
# "test".title()        = Test
# "test".upper()        = TEST
#

