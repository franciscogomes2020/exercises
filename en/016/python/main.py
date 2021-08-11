# Create a program that reads any Real number from the keyboard and displays its Integer portion on the screen.

from math import floor

number = float( input( ' type a real number ' ) )
number = floor( number )
print(' the integer part of the typed number is {}'.format( number ) )

# OUTPUT -->
# type a real number 7.8
# the integer part of the typed number is 7
