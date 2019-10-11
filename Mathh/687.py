# You are given an array of numbers. Print the least occurring element. 
# If there is more than 1 element print all of them in decreasing order of their value.

# Input Description:
# You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

# Output Description:
# Print the number as mentioned

# Sample Input:
# 9
# 1 6 4 56 56 56 6 4 2

# Sample Output:
# 2 1

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

nums = {}

for i in reversed(range(n)):
    if nums[arr[i]]>0:
        temp = nums[arr[i]]
        nums[arr[i]] = temp+1
    else:
        temp = 0 
        nums[arr[i]] = temp+1



