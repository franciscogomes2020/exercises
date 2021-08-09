# Write a program that reads the width and height of a wall in meters. 
# Calculate its area and the amount of paint needed to paint it. 
# Knowing that each liter of paint paints an area of 2m².

width = float( input(' What is the width in meters of the wall? ') )
height = float( input(' What is the height in meters of the wall? ') )

area = width * height
liters = area / 2

print(' You will need {} liters of paint to paint that wall '.format(liters) )

# OUTPUT -->
# What is the width in meters of the wall? 5.45
# What is the height in meters of the wall? 2.80
# You will need 7.63 liters of paint to paint that wall
