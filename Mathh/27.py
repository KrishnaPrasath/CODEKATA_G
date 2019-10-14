# Given 2 numbers N and K followed by N elements, print the number of repetition of K otherwise print '-1' if the element not found.
# Sample Testcase:
# INPUT
# 6 2
# 1 2 3 5 7 8
# OUTPUT
# 0

#done alrdy

N, K = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for each in range(N):
    if arr[each] == K:
        count += 1

if count == 0:
    print(-1)
else:
    print(count-1)
