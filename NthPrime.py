# Project Euler Problem 7
from mytc import Test
from itertools import count

def NthPrime(n: int) -> int:
    primes = []
    for num in count(2):
        if len(primes) == n:
            return num - 1
        tf = DivisibleByFactors(num, primes)
        if tf:
            continue
        primes.append(num)

def DivisibleByFactors(n: int, factors: list) -> bool:
    for p in factors:
        if n % p == 0:
            return True
    return False
    
if __name__ == "__main__":
    tc = {
        6: 13,
        10: 29,
        100: 541,
        1000: 7919,
        10001: 104743,
    }

    Test(tc, NthPrime)

# def NthPrime(n):
#     primes = []
#     for num in count(2):
#         if len(primes) == n:
#             return num - 1
#         if not [p for p in primes if num % p == 0]:
#             primes.append(num)
#             # print(primes)