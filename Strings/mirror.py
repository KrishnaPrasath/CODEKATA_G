# Given 2 arrays print yes if they are mirror images of each other, otherwise no.
# Input Size: N <= 1000000
# Sample Testcase:
# INPUT
# 4
# 1 2 3 4
# 4 3 2 1
# OUTPUT
# yes

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def checkMirror(N, A, B):
    for i in range(N):
        if A[i] != B[(N-1)-i]:
            return False
    return True


if checkMirror(N, A, B):
    print('yes')
else:
    print('no')

