# You are an employee of ‘Rox Travel’ channel.The channel has decided to give allowances to some customer who satisfy these conditions. The conditions are:

# The customer should be born on or before july 22 1987

# The month of D.O.B month should be of 31 days.

# You are given with the D.O.B of all the employees.Your task is to print the employee index who are having chance to avail special offer.

# Input Description:
# First line contains the number of employee.Next line contains an array of D.O.B of employees

# Output Description:
# Print the employee index(index at 1). Print-1 if there are no such employee

# Sample Input:
# Input
# 4
# 23 MARCH 1996 23 MARCH 1986 22 JULY 1987 23 APRIL 1987

# Sample Output:
# 2 3

# TODO check with JOHN
import re

N = int(input())
dob = input()  # 23 MARCH 1996  
# date[], month[], year[] = 

months = "JANUARY,MARCH,MAY,JULY,AUGUST,OCTOBER,DECEMBER".split(',')

bMonths = "JANUARY,MARCH,MAY,JULY".split(',')
output = []
# dob = list(map(str, input().split(' ')))

result = re.findall("\d{2}\s[a-zA-Z]{3,}\s\d{4}", dob)

final = []
for each in result:
    final.append(each.split(' '))

for each in final:
    if int(each[2]) <= 1987:
        if int(each[2]) == 1987 and each[1] in bMonths:
            output.append(final.index(each)+1)
        elif each[1] in months:
            output.append(final.index(each)+1)

if len(output) > 0:
    print(*output)
else:
    print(-1)
