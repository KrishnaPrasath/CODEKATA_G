vowels = 'a,e,i,o,u'.split(',')
N = int(input())
arr = []
for i in range(N):
    temp = input()
    arr.append(temp)

print(arr)


def checkVowels(arr):

    count = 0
    for each in arr:
        flag = False
        for ch in each:
            if ch in vowels:
                flag = True
        if flag:
            count += 1
    return count


if checkVowels(arr) == N:
    print('yes')
else:
    print('no')
