# Project Euler Problem 3
from mytc import Test

def Sieve(n):
    if_prime = [1 for i in range(n)]
    current = 2
    while current**2 <= n:
        if if_prime[current] == 1:
            for mult in range(current * 2, n, current):
                if_prime[mult] = 0
        current += 1
    primes = [i for (i, p) in list(enumerate(if_prime)) if p == 1] # List of only prime numbers
    return primes[2:]

primenumbers = Sieve(7000) # Only works with prime numbers not exceeding 7000


def LargestPrimeFactor(num) -> int:
    gpf = 1
    for prime in primenumbers:
        if num % prime == 0:
            gpf = prime
    return gpf

if __name__ == "__main__":
    tc = {
        2: 2,
        3: 3,
        5: 5,
        7: 7,
        20: 5,
        13195: 29,
        600851475143: 6857,
    }

    Test(tc, LargestPrimeFactor)



# def LargestPrimeFactor(n) -> int:
#     facs = []
#     for i in range(2, n+1):
#         if n % i == 0:
#             if isPrime(i):
#                 facs.append(i)
#     if len(facs) == 0:
#         return 1
#     return max(facs)

# def isPrime(n) -> bool:
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def lisp(num) -> int:
#     ints = [1 for i in range(num + 1)] # all ints up to n get a 1
#     p = 2
#     while p**2 <= num:
#         if ints[p] == 1:
#             for i in range(p * 2, num + 1, p):
#                 ints[i] = 0
#         p = p + 1
#     ints = list(enumerate(ints[1:], 1))
#     things = [i for (i, p) in ints if p == 1 and num % i == 0]
#     return max(things)