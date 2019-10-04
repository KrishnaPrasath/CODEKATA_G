# Given an array N, sort it in ascending order till it reaches kth elements and after that sort it in descending order.
# Input Size: N <= 100000
# Sample Testcase:
# INPUT
# 5 2
# 4 3 1 2 4
# 4 3 1
# OUTPUT
# 3 4 4 2 1

N, K = map(int, input().split())
arr = list(map(int, input().split()))
min = arr[0]


def swap(a, b):
    a = a+b
    b = a-b
    a = a-b


def sortAsc(arr):
    for i in range(N):
        min_index = i
        for j in range(i+1, N):
            if arr[min_index] > arr[j]:
                min_idx = j
        swap(arr[i], arr[min_idx])


sortAsc(arr)
print(arr)

