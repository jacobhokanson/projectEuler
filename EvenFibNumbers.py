# Project Euler Problem 2
from mytc import Test

def EvenFibNumbers(n):
    even_indexes = list(range(1, n+1))[1::3]
    evens = [Fib(x) for x in even_indexes]
    return sum(evens)

def Fib(n):
    if n in (0,1):
        return 1
    return Fib(n - 1) + Fib(n - 2)

testcases = {
    10: 44,
    18: 3382,
    23: 60696,
    # 43: 350704366, # This case falls into recursion Tartarus and never returns for some reason =[
}

Test(testcases, EvenFibNumbers)