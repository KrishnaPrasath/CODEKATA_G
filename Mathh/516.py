#  co-prime
# If GCD of a couple of numbers is 1, then both the numbers are a co prime

# print yes or no
# done 10coins

a, b = map(int, input().split())


def getDivisors(a):  # 123
    divisors = []
    for i in range(1, a):
        if a % i == 0:
            divisors.append(i)
    return divisors


def gcd(a, b):

    A = getDivisors(a)
    B = getDivisors(b)
    x = set(A)
    y = set(B)
    return(x.union(y))


C = list(gcd(a, b))

print(1) if len(C) == 1 and C[0] == 1 else print(1)
