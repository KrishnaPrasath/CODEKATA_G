# check if a string us wonderful or not

# a string is wonderful if it is made up of only 3 chars
# done
try:
    s = input()
except EOFError as e:
    print(-1)
dic = {}
temp = 0
for each in s:
    if each in dic:
        temp = dic[each]
        dic[each] = temp+1
    else:
        temp = 0
        dic[each] = temp+1

if len(dic) == 3:
    print('Wonder')
else:
    print(-1)
