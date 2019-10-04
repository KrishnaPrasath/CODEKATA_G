# Given a number N, print the sum of the squares of its digits.
# Input Size : 1 <= N <= 1000000000000000000
# Sample Testcase :
# INPUT
# 19
# OUTPUT
# 82
# pblm num 73
# done
import math
N = int(input())
digits = []
while N > 0:
    temp = math.floor(N % 10)
    digits.append(temp)
    N = math.floor(N/10)
sum = 0
for each in digits:
    sum += (each**2)
print(sum)
