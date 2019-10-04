# Roman Reigns want to write a program that identify the repeated letters and capitalize it.Help him to achieve it.
# Sample Testcase:
# INPUT
# computer program
# OUTPUT
# cOMPuteR PROgRaM
#check with JOHN
s = input()
sList = list(s)


def catchRep(s):
    dic = {}
    temp = 0
    for each in s:
        if each in dic:
            temp = dic[each]
            dic[each] = temp+1
        else:
            temp = 0
            dic[each] = temp+1
    return dic


def cap(dic, lis):
    for k in dic:
        if dic[k] > 1:
            lis = [i.upper() if i == k else i for i in lis]
    return lis


dic = catchRep(s)
result = cap(dic, sList)


print(''.join(result))
