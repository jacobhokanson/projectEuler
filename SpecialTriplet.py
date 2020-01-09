# Project Euler Problem 9
from mytc import Test
from math import floor

def SpecialTriplet(n):
    min, max = int(floor(n / 3 + 1)), int((n + .1)//2 - 1)
    a, b = 3, max - 1
    possible_c = [c for c in range(max, min - 1, -1)]
    for i in range(len(possible_c)):
        a = 3 + 2 * i
        b = max - 1 * (i + 1)
        while a < b:
            # print(f'trying {a} {b} for {possible_c[i]}')
            if a**2 + b**2 == possible_c[i]**2:
                return a * b * possible_c[i]
            a, b = a + 1, b - 1

if __name__ == "__main__":
    tc = {
        24: 480,
        120: 49920,
        1000: 31875000,
    }

    Test(tc, SpecialTriplet)


# while not a+1 >= b:
#     while not a == c - 1:
#         print(f'testing {a} {b} {c}')
#         if a**2 + b**2 == c**2:
#             return a*b*c
#         a, b = a + 1, b - 1
#     a, b, c = a + 2, b - 1, c - 1
# print("nope")
# return a*b*c