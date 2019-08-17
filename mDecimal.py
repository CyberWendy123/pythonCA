# Ch 7: Modules (Aug 17, 2019) 
#	via 4. Modules Python Decimals 

# Import Decimal below:
from decimal import Decimal

# Original: 
two_decimal_points = 0.2 + 0.69
print(two_decimal_points)

four_decimal_points = 0.53 * 0.65
print(four_decimal_points)

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
# my problem: I forgot to turn the numbers into strings  