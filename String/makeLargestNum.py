# Given a number N followed by N numbers. Find the largest number which can be formed from the given numbers and print it.
# NOTE: Each number should be used exactly once.
# Input Size: 1 <= N <= 100000
# Sample Testcases:
# INPUT
# 5
# 5 6 7 8 9
# OUTPUT
# 98765

# input
N = int(input())
arr = map(int, input().split())

# op
dic = {}
lis = []
for each in arr:
    dic[each] = 1

for each in dic:
    lis.append(each)

# sort


def sortNum(lis):
    for i in range(N):
        for j in range(N-i):
            if lis[i] < lis[j]:
                temp = ''
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp


print(sortNum(lis))
