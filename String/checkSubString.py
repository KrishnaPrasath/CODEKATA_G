<<<<<<< HEAD
# Given 2 strings of length N,M check if the second string is a substring of the first string.
# Input Size : 1 <= N <= 100000
# Sample Testcase :
# INPUT
# Banana ana
# OUTPUT
# yes
# Done
A, B = map(str, input().split())
N = len(A)
M = len(B)


def checkSub(a, b):
    if b in a:
        print('yes')
    else:
        print('no')


if N >= 1 and N <= 100000:
    checkSub(A, B)
=======
# Given 2 strings of length N,M check if the second string is a substring of the first string.
# Input Size : 1 <= N <= 100000
# Sample Testcase :
# INPUT
# Banana ana
# OUTPUT
# yes

A, B = map(str, input().split())
N = len(A)
M = len(B)


def checkSub(a, b):
    if b in a:
        print('yes')
    else:
        print('no')


if N >= 1 and N <= 100000:
    checkSub(A, B)
>>>>>>> 1da576e8c875a839b18cbe0d79539ed735d47206
