
string = "cocomomokon"
dic = dict()
count = 0

for i in range(len(string)):
    if string[i] in dic:
        temp = dic[string[i]]
        temp += 1
        dic[string[i]] = temp
    else:
        dic[string[i]] = 1

# for key, value in dic.items():
#     if value < maxVal:
#         maxVal = value
# print(maxVal)
minVal = min(dic, key=dic.get)
values = dic.get(minVal)
print(values)
