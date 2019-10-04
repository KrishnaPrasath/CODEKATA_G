import math
N = int(input())
digits = []
dic = dict()
flag = True
while N > 0:
    temp = math.floor(N % 10)
    digits.append(temp)
    N = math.floor(N/10)

for i in range(len(digits)):
    char = digits[i]
    if char in dic:
        temp = dic[char]
        temp += 1
        dic[char] = temp
    else:
        temp = 1
        dic[char] = temp

for each in dic:
    if dic[each] > 1:
        flag = False

if flag:
    print('no')
else:
    print('Yes')
