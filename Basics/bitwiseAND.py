# BitWise AND

# INPUT
# 2
# 2 4
# OUTPUT
# 0

N = int(input())
lis = list(map(int, input().split()))

for i in range(N):
    print(lis[i] & lis[i+1])

# print(lis[0] & lis[1])
