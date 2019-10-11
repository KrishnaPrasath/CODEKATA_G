# Given a number N, find the nearest greater multiple of 10.
# Input Size: N <= 10000
# Sample Testcase:
# INPUT
# 3
# OUTPUT
# 10

# done 20c

N = int(input())

if N % 10 == 0:
    print(N)
elif N > 10:
    temp = N % 10
    diff = 10 - temp
    print(N+diff) if diff < 5 else print(N-temp)
else:
    diff = 10 - N
    print(N+diff)
