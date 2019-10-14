# # Given a number N, check whether it is prime or not.Print 'yes' if it is prime else print 'no'.
# Sample Testcase :
# INPUT
# 123
# OUTPUT
# no

#done 30c

n = int(input())


def prime(n):
    for each in range(2, n):
        if n % each == 0:
            return False
    return True


if prime(n):
    print('yes')
else:
    print('no')
