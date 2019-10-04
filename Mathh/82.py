# Given a number and a number of K, find the greatest number which divides both.
# Input Size : N and K <= 100000
# Sample Testcase :
# INPUT
# 5 10
# OUTPUT
# 5
# dine
N, K = map(int, input().split())
minVal = min(N, K)
divLis = []
for i in range(1, minVal+1):
    for j in range(1, minVal+1):
        if i * j == minVal:
            divLis.append(i)

print(max(divLis))
