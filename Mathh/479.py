# Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory.


# CONSTRAINTS

# 1<=Y,N,T<=1000

# Input Description:
# First line contains no. of test cases(Y). Next line contains a number N. Next line contains n space separated numbers Next line contains a number T denoting the number of questions asked from you regarding the given array. Next line contains T space separated numbers.

# Output Description:
# Print the occurrence of each number if present else “NOT PRESENT”

# Sample Input :
# 10
# 1 1 1 2 2 2 3 8 9 7
# 5
# 1 2 3 0 5

# Sample Output :
# 3 3 1 Not Present Not Present

Y = int(input())
N = list(map(int, input().split()))
T = int(input())
tArr = list(map(int, input().split()))

dic = {}
for i in range(Y):
    count = 0
    if(dic[N[i]]>0):
        count = dic[N[i]]+1
        dic[N[i]] = count
    else:
        count = 0
        dic[N[i]] = count

for i in range(T):
    if(dic[N[i]]):
        print(dic[tArr[i]], end=" ")
    else:
        print('NOT PRESENT', end=" ")
