# Given a number N, print the product of the digits.
# Input Size: N <= 100000000000
# Sample Testcase:
# INPUT
# 2143
# OUTPUT
# 24
# done 20c


def prodDigit(n):
    result = 1
    while n > 0:
        temp = n % 10
        result *= temp
        n //= 10
    print(result)


N = int(input())

prodDigit(N)
