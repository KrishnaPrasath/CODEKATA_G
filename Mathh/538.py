# You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which
# is made by exactly two digits.

# Input Description:
# You are given with a number n.

# Output Description:
# Print Saturated if it is Saturated else it is Unsaturated

# Sample Input:
# 121

# Sample Output:
# Saturated

# done 10c

# TODO : capitalize saturated to match the test case

n = input()
result = {}


def satur(N, dic):
    for each in N:
        dic[each] = 'exist'
    if len(dic) == 2:
        print('saturated')
    else:
        print('Unsaturated')


satur(n, result)
