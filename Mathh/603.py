# In a world cup tournament,no of goals scored by each team is given to you. Your task is to calculate net goal rate of each team.

# Net goal rate of team is calculated


# No of goals(team)- sum of(no of goals by last 3 teams)

# Input Description:
# You are given a number ‘n’.Next line contains n space separated numbers.

# Output Description:
# Print the net goal rate of each team

# Sample Input :
# 5
# 95 85 75 12 11

# Sample Output :
# -3 -13 -23 -74 -76

# TODO

n = int(input())
goals = list(map(int, input().split()))


def calc(n, G):

    total = sum([G[i] for i in reversed(range(n-3, n))])

    return [i-total for i in G]


print(calc(n, goals))
