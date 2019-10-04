# Given 2 numbers N,M. Find their difference and check whether it is even or odd.
# Sample Testcase :
# INPUT
# 5 5
# OUTPUT
# even
# done
N, M = map(int, input().split())
diff = N-M
if diff % 2 == 0:
    print('even')
else:
    print('odd')
