# Create an algorithm that reads a number and displays its double, triple and square root.

number = int ( input(' type a number: ') )
double = number * 2
triple = number * 3
square = number ** (1/2)

print( ' number: {}\n double: {}\n triple: {}\n square: {}'.format(number, double, triple, square) )

# OUTPUT -->
# type a number: 25
# number: 25
# double: 50
# triple: 75
# square: 5.0
