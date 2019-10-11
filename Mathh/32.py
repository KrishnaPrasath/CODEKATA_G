# Write a program to print the sum of the first K natural numbers.
# Input Size: n <= 100000
# Sample Testcase:
# INPUT
# 3
# OUTPUT
# 6

# alrdy done

N = int(input())


def sumOfNum(N):
    result = 0
    for i in range(N+1):
        result += i
    print(result)


sumOfNum(N)
