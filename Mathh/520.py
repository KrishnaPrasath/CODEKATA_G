# Simi is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.Simi has told you about this and want your help. You design an algorithm in order to help simi.

# Input Description:
# You will be given a number ‘n’

# Output Description:
# Print the count of all palindromic numbers till ‘n’(inclusive)

# Sample Input :
# 5

# Sample Output :
# 5

# TODO check with john

n = int(input())


def check(n):
    temp = 0
    x = n
    while x > 0:
        temp += x % 10
        if x > 10:
            temp *= 10
        x //= 10
    return True if n == temp else False


def checkPal(n):
    result = []
    for x in range(n):
        if x < 10 and x >= 0:
            result.append(x)
        elif check(x):
            result.append(x)
    print(len(result))


checkPal(n)
