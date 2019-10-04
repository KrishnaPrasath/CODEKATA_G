<<<<<<< HEAD
# Given a string s swap the even and odd characters.Assume the index starts from 0.
# Input Size: | s | <= 10000000(complexity O(n))
# Sample Testcase:
# INPUT
# codekata
# OUTPUT
# ocedakat
# done

string = input()
lis = []
result = ''
for each in string:
    lis.append(each)

for i in range(len(string)):
    if not i % 2 == 0:
        temp = ''
        temp = lis[i]
        lis[i] = lis[i-1]
        lis[i-1] = temp

result = ''.join(lis)
print(result)
=======
# Given a string s swap the even and odd characters.Assume the index starts from 0.
# Input Size: | s | <= 10000000(complexity O(n))
# Sample Testcase:
# INPUT
# codekata
# OUTPUT
# ocedakat

string = input()
lis = []
result = ''
for each in string:
    lis.append(each)

for i in range(len(string)):
    if not i % 2 == 0:
        temp = ''
        temp = lis[i]
        lis[i] = lis[i-1]
        lis[i-1] = temp

result = ''.join(lis)
print(result)
>>>>>>> 1da576e8c875a839b18cbe0d79539ed735d47206
