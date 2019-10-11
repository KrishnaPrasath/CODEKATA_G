# You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

# m+j=n


# Input Description:
# You are given a number n;

# Output Description:
# Print Great if a number is great else print the no

# Sample Input :
# 59

# Sample Output :
# Great

N = int(input())
m = 0
j = 1


def sumOfDigits(N, m):
    m = 0
    while N > 0:
        m += N % 10
        N //= 10
    return m


def productOfDigits(N, j):
    j = 1
    while N > 0:
        j *= N % 10
        N //= 10
    return j


m = sumOfDigits(N, m)
j = productOfDigits(N, j)
print('Great') if m+j == N else print('no')
