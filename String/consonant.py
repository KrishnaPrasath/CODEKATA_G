# print only the consonant
# one test case passed
vowels = "aeiouAEIOU"

string = input()
lis = []
for i in range(len(string)):
    temp = string[i]
    if not temp in vowels:
        lis.append(temp)


result = "".join(lis)

print(result.strip())
