# Create a program that reads how much money a person has in their wallet and displays how much Reais they can buy. Consider U$1.00 = R$3.27.

## Example in Python
### Code

``` python
dollar = float( input(' How much money do you have? ') )
usdbrl = 3.27
print(' you can buy {:.2f} Reals'.format(dollar * usdbrl ) )
```

### Output

```
 How much money do you have? 2.00
 you can buy 6.54 Reals
```
