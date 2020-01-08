# Project Euler Problem 5
from mytc import Test

def sm(n):
    if n == 1:
        return 1
    prev = sm(n-1)
    for i in range(prev, prev*n+1, prev):
        if i % n == 0:
            return i

if __name__ == "__main__":
    tc = {
        1: 1,
        2: 2,
        3: 6,
        4: 12,
        5: 60,
        7: 420,
        10: 2520,
        13: 360360,
        20: 232792560,
    }

    Test(tc, sm)

# ARCHIVES

# for i in count(1):
#     print(c, "-", i, "times sm(" + str(n-1) + ")")
#     if i * sm(n-1) % n == 0:
#         return i * sm(n-1)

# def SmallestMultiple(n):
#     for i in range(1, factorial(n)+1):
#         if not [p for p in range(1, n+1) if not i % p == 0]: # listcomp gives any nums from 1 to n that do not divide
#             return i
# 
#     [i for i in range(1, f(o)+1) if [p for p in range(1, o+1) if not i % p == 0] == []]

# def SmallestMultiple(n): # Returns smallest positive integer evenly divisible by all numbers from 1 to n
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return (SmallestMultiple(n - 1) * n) / 