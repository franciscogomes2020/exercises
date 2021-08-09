# Write a program that reads a value in meters and displays it coverted to centimeters and milimeters

## Example in Python

### Code

``` python
meter = float( input(' type a value in meters: ').replace(',','.') )
centimeter = meter * 100
milimeter  = meter * 1000

print(' centimeters: {}\n milimeters: {}'.format(
    centimeter - int(centimeter) == 0 and int(centimeter) or centimeter,
    milimeter - int(milimeter) == 0   and int(milimeter)  or milimeter
    ) )
```

### Output

```
 type a value in meters: 1,25
 centimeters: 125
 milimeters: 1250
```
