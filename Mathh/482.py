N = int(input())


def calcSavings(N):
    a = 0
    init = 1
    savings = 0
    for i in range(N+1):
        savings = a+init
        init = a + init
        a = init
    print(savings)


calcSavings(N)
