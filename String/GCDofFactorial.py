# Given 2 numbers A,B. Print the GCD of a!,b!.
# Input Size : B <= 10 <= A <= 1000000000
# Sample Testcase :
# INPUT
# 4 2
# OUTPUT
# 2

A, B = map(int, input().split())
divList = []
result = []


def checkIP(a, b):
    if a == 0 or b == 0:
        return False
    return True


def factors(N):
    fact = []
    temp = 1
    for i in range(1, N+1):
        fact.append(i)
    return fact


def findDiv(N):
    divisors = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j == N:
                divisors.append(i)
    return divisors


def findMax(lis):
    maxVal = 0
    for each in lis:
        if each > maxVal:
            maxVal = each
    return maxVal


def findMin(a, b):
    if a < b:
        return a
    else:
        return b


if checkIP(A, B):
    print(findMax(factors(findMin(A, B))))
else:
    print(0)
