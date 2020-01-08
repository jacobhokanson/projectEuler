# Project Euler Problem 6
from mytc import Test

def sumSquareDifference(n):
    return sum(range(n+1))**2 - sum([i**2 for i in range(n+1)])

tc = {
    10: 2640,
    20: 41230,
    100: 25164150,
}

Test(tc, sumSquareDifference)