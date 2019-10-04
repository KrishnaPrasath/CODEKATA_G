# Given a number N followed by a list of N numbers. Write a program to reverse the list and print the list.
# Input Size: 1 <= N <= 10000
# Sample Testcases:
# INPUT
# 7
# 1 2 3 4 5 6 7
# OUTPUT
# 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
N = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = []
for i in reversed(range(N)):
    if i != 0:
        print('%d->' % arr[i], end='')
    else:
        print(arr[i])

