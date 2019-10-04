# Given a number N and an array of N strings, find the number of strings that are an anagram of 'kabali'.
# Input Size: 1 <= N <= 1000
# Sample Testcase:
# INPUT
# 5
# kabali
# kaabli
# kababa
# kab
# kabail
# OUTPUT
# 3

# N = int(input())
N = 5
arr = ["kabali",
       "kaabli",
       "kababa",
       "kab",
       "kabail"]
string = 'kabali'
# N = int(input())
# arr = []
# string = 'kabali'
# for i in range(N):
#     arr.append(input())
dictionary = dict()
count = 0

for ch in string:
    if ch in dictionary:
        count += 1
    else:
        count = 1
    dictionary[ch] = count


def checkAnagram(dic, arr):
    result = dict()

    for each in arr:
        if(len(each) < len(string) or len(each) > len(string)):
            break
        for i in dic:
            temp = dic[i]
            if i in each:
                temp += 1
            result[i] = temp
        print(result)


print(checkAnagram(dictionary, arr))
