# You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1

# Input Description:
# A large number ‘n’

# Output Description:
# Print the max no of consecutive 1 in the number

# Sample Input :
# 101011111

# Sample Output :
# 5

# Done 10c

n = input()
result = []
count = 0
maxC = 0
for i in range(len(n)):
    if int(n[i]) == 1:
        count += 1
        maxC = count
    elif int(n[i]) == 0:
        if count > maxC:
            maxC = count
        count = 0


if maxC > 0:
    print(maxC)
else:
    print(-1)
