# Given a number N, print the even factors of the number.
# Input Size: 1 <= N <= 1000
# Sample Testcase:
# INPUT
# 8
# OUTPUT
# 2 4 8

N = int(input())

factors = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if i * j == N:
            if i % 2 == 0:
                factors.append(i)
print(*factors)
