# Make a program that reads any integer and displays its times tables on the screen.

number = int( input(' type a integer: ') )

for i in range(11):
    print(' {:>2} x {} = {}'.format(i, number,i*number) )

# OUTPUT --> typed 5
# type a integer: 5
#  0 x 5 = 0
#  1 x 5 = 5
#  2 x 5 = 10
#  3 x 5 = 15
#  4 x 5 = 20
#  5 x 5 = 25
#  6 x 5 = 30
#  7 x 5 = 35
#  8 x 5 = 40
#  9 x 5 = 45
# 10 x 5 = 50
