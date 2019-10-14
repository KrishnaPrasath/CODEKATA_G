# Ajay is given a series(In example).he gone through the series but unable to understand it properly,
# he has hired you.Your task is to understand the series and print the .You are given with a number ‘n’.
# Find the nth number of series.

# Input Description:
# You are given a number ‘n’.

# Output Description:
# Print the nth number of series

# Sample Input:
# 3

# Sample Output:
# 108

# 12 36 108

n = int(input())

a = n*4


def series(n, a):
    for i in range(n-1):
        a = n*a
    print(a)


series(n, a)
