'''
Instructions
Output
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

like:
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
'''

import math
def zeros(n):
    m = 0 
    num = math.factorial(n)
    for i in list(str(num))[::-1]:
        if int(i) == 0:
            m += 1
        else:
            break
    return m
