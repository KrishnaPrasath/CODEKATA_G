# Given a number N,print the reverse of the number N.
# Sample Testcase :
# INPUT
# 423
# OUTPUT
# 324
# done

import math
N = int(input())
while N > 0:
    print(N % 10, end="")
    N = math.floor(N/10)
