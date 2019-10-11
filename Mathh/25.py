# Find the minimum among 10 numbers.
# Sample Testcase :
# INPUT
# 5 4 3 2 1 7 6 10 8 9
# OUTPUT

# 1
# done

arr = list(map(int, input().split()))
minN = arr[0]

for each in arr:
    if each < minN:
        minN = each

print(minN)
