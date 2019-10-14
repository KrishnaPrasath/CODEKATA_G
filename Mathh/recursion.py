# recursion
num = 3


def fun(n):
    if(n == 1):
        return n
    return n*fun(n-1)

print(fun(num))

