# Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
# Input Size: N <= 100000
# Sample Testcase:
# INPUT
# 2143
# OUTPUT
# 1 3

N = input()

countOfOdd = []


def checkOdd(N, countOfOdd):
    for each in N:
        if int(each) % 2 != 0:
            countOfOdd.append(int(each))
    # countOfOdd = [i for i in N if int(i) % 2 != 0]


checkOdd(N, countOfOdd)


if countOfOdd == 0:
    print(-1)
else:
    print(*countOfOdd)
