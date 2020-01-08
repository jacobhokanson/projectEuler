# Project Euler Problem 4
from mytc import Test

def PalindromeProduct(n):
    if n == 1:
        return 9
    else:
        test_num = int('9' * n) ** 2
        while True:
            while not testPalindrome(test_num):
                test_num -= 1
            print("trying", test_num, "- checking for factors...")
            for fac1 in range(int('9' * n), int('9' * (n - 1)), -1):
                if test_num % fac1 == 0:
                    print(" -", fac1, "is a factor...it's complement is", test_num // fac1)
                    if len(str(test_num // fac1)) == n: # fac2
                        return test_num
            test_num -= 1
    return None

def testPalindrome(n):
    n = str(n)
    return n[:len(n)//2] == n[-(len(n)//2):][::-1]

if __name__ == "__main__":
    tc = {
        1: 9,
        2: 9009,
        3: 906609,
    }

Test(tc, PalindromeProduct)

# pa = {
#     "lol": True,
#     "lool": True,
#     "this": False,
#     "operepo": True,
#     111: True,
#     121: True,
#     122: False
# }

# Test(pa, testPalindrome)