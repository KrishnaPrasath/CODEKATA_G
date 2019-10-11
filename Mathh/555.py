# Assume that you are ticket verifier at a club. Your club has decided to give a special discount to the person(s) who are satisfying the following condition


# Condition: -

# If ticket number is divisible by date of month. You are eligible for a discount.

# Input Description:
# First line contains input ‘n’.Next line contains n space separated numbers denoting ticket numbers .Next line contains ‘k’ date of the month.

# Output Description:
# Print 1 if the ticket is eligible for discount else 0

# Sample Input:
# 6
# 112 139 165 175 262 130
# 22

# Sample Output:
# 0 0 0 0 0 0

#TODO check testcases   

n = int(input())
ticketNums = list(map(int, input().split()))
date = int(input())

def ticketValidation(n, nums, date):
    for i in range(n):
        if nums[i] == 0 :
            print(0,end=' ')
        elif nums[i]==0 and i == n-1:
            print(0,end='')
        elif i == n-1:
            print(1, end='') if nums[i] % 22 == 0 else print(0, end='')
        else:
            print(1, end=' ') if nums[i] % 22 == 0 else print(0, end=' ')

ticketValidation(n, ticketNums, date)
