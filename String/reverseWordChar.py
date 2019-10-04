<<<<<<< HEAD
# Given a string S of length N, reverse every word in place.
# Input Size: 1 <= N <= 100000
# Sample Testcase:
# INPUT
# abcd er x
# OUTPUT
# dcba re x
# done

S = list(map(str, input().split()))
result = []
for each in S:
    temp = ''
    for i in reversed(range(len(each))):
        temp += each[i]
    result.append(temp)

print(*result)
=======
# Given a string S of length N, reverse every word in place.
# Input Size: 1 <= N <= 100000
# Sample Testcase:
# INPUT
# abcd er x
# OUTPUT
# dcba re x

S = list(map(str, input().split()))
result = []
for each in S:
    temp = ''
    for i in reversed(range(len(each))):
        temp += each[i]
    result.append(temp)

print(*result)
>>>>>>> 1da576e8c875a839b18cbe0d79539ed735d47206
