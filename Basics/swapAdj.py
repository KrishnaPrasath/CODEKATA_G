# Given an array of numbers switch(swap) the adjacent characters.
# Sample Testcase :
# INPUT
# 5
# 3 2 1 2 3
# OUTPUT
# 2 3 2 1 3
#done but no points - #basic
N = int(input())
lis = list(map(int, input().split()))


def swapAdjacent(N, arr):
    for i in range(0, N):
        if not i % 2 == 0:
            arr[i-1] = arr[i]+arr[i-1]
            arr[i] = arr[i-1] - arr[i]
            arr[i-1] = arr[i-1] - arr[i]

    print(*arr)


swapAdjacent(N, lis)

