<<<<<<< HEAD
# Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1
# Input Size : |s| <= 100000
# Sample Testcase :
# INPUT
# codekata a
# OUTPUT
# 2
# done

S, K = map(str, input().split())
count = 0

for each in S:
    if K == each:
        count += 1

if count == 0:
    print(-1)
else:
    print(count)
=======
# Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1
# Input Size : |s| <= 100000
# Sample Testcase :
# INPUT
# codekata a
# OUTPUT
# 2
S, K = map(str, input().split())
count = 0

for each in S:
    if K == each:
        count += 1

if count == 0:
    print(-1)
else:
    print(count)
>>>>>>> 1da576e8c875a839b18cbe0d79539ed735d47206
