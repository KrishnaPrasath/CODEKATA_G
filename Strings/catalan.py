# (2n)!/n!(n+1)!
import math
n = int(input())


def fact(N):
    fact = 1
    for i in range(N):
        fact *= (i+1)
    return fact


def catalan(n):

    return math.floor(fact(2*n)/(fact(n)*fact(n+1)))


print(catalan(n))
