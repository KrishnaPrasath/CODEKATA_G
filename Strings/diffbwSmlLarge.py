# Given a number N and array of N integers, print the difference between the smallest and largest number.
# done
N = int(input())
nArr = list(map(int, input().split()))

temp = nArr.copy()

temp.sort()

sml = temp[0]
big = temp[N-1]

print(big-sml)
