# Sreelatha was confused with series. She is given with a number ‘n’. There is a pattern hidden the series. She has to understand and print the series till nth number by looking into example.Sreelatha is confused and She hired you, you have to develop the series for sreelatha by observing the pattern from the below example.

# Input Description:
# She is given with a number ‘n’.

# Output Description:
# print the series till nth number

# Sample Input:
# 3

# Sample Output:
# 1 9 36

N = int(input())
result = []
result.append(1)
temp = 3
while N > 1:
    result.append(pow(temp, 2))
    temp += 3
    N -= 1

if N==0:
    print(0)
else:
    print(*result)
