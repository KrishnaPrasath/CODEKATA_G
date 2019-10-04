# 28
# Count the number of digits of a given number N.Size of the integer ranges from 1Sample Testcases :
# INPUT
# 548
# OUTPUT
# 3
# done
import math
N = int(input())
digits = 0
if N == 0:
    digits = 0
else:
    while N > 0:
        temp = math.floor(N % 10)
        digits += 1
        N = math.floor(N/10)

print(digits)
