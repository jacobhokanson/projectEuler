# Project Euler Problem 10 # woot woot
from mytc import Test

def SumPrimes(n: int) -> int:
    r = [1 for i in range(n)]
    index = 2
    while index**2 <= n:
        if r[index] == 1:
            for m in range(index * 2, n, index):
                r[m] = 0
        index += 1
    return sum([i for (i, p) in enumerate(r) if p == 1][2:])

if __name__ == "__main__":
    tc = {
        17: 41,
        2001: 277050,
        140759: 873608362,
        2000000: 142913828922,
    }

    Test(tc, SumPrimes)