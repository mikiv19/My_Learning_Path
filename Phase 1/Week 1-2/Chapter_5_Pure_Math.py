"Chapter 5 - Pure math"

"An Algorithm for Generating Continued Fractions"
import math

x = 105
y = 33
big = max(x,y)
small = min(x,y)

output = []
quotient = math.floor(big/small)
output.append(quotient)

new_small = big % small
big = small
small = new_small

def continued_fraction(x,y,length_tolerance):
    output = []
    big = max(x,y)
    small = min(x,y)

    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big % small
        big = small
        small = new_small
    return(output)
print(continued_fraction(105,33,10))
'''
We may want to check that a particular continued fraction correctly
expresses a number we’re interested in. In order to do this, we should
define a get_number() function that converts a continued fraction to a decimal number
'''
def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]  
    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1/number + next
        index -= 1
    return(number) 
get_number([3,5,2])

"From Decimal to Continued Fractions"
x = 1.4142135623730951
output = []
first_term = int(x)
leftover = x - int(x)
output.append(first_term)
next_term = math.floor(1/leftover)
leftover = 1/leftover - next_term
output.append(next_term)

def continued_fraction_decimal(x,error_tolerance,length_tolerance):
    output = []
    first_term = int(x)
    leftover = x - int(x)
    output.append(first_term)
    error = leftover
    while error > error_tolerance and len(output) <length_tolerance:
        next_term = math.floor(1/leftover)
        leftover = 1/leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)
    return(output)
print(continued_fraction_decimal(1.4142135623730951,0.00001,100))