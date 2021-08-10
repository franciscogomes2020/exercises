# Write a program that asks how many kilometers a rental car has traveled and how many days it has been rented. Calculate the price to pay, knowing that the car costs $60 per day and $0.15 per mk driven.

## Example in Python

### Code

``` python
days      = int( input( ' How many days has the rental car rented? ') )
kms       = float( input( ' How many kms has the rental car traveled? ') )
dayRental = 60
kmRental  = 0.15
dayRent   = dayRental * days
kmRent    = kmRental * kms

print('-' * 60)
print(' {} days rented, the price a day is {}, total: {}'.format(days,dayRental,dayRent) )
print(' {} kms traveled, the price per km is {}, total: {}'.format(kms,kmRental,kmRent) )
print(' total to pay is {:.2f} '.format(dayRent + kmRent) )
```
### Output

```
 How many days has the rental car rented? 7
 How many kms has the rental car traveled? 700
------------------------------------------------------------
 7 days rented, the price a day is 60, total: 420
 700.0 kms traveled, the price per km is 0.15, total: 105.0
 total to pay is 525.00

```

[List of Exercises](../..)
