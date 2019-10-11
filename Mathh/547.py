# In XYZ country there is rule that car’s engine no. depends upon car’ number plate. Engine no is sum of all
# the integers present on car’s Number plate.
# The issuing authority has hired you in order to provide engine no. to the cars.Your task is to
# develop an algorithm which takes input as in form of string(Number plate) and gives back

# Engine number.

# Input Description:
# You are given a string ’s’

# Output Description:
# Print the number plate

# Sample Input:
# HR05-AA-2669

# Sample Output:
# 28
# done 10c

s = input()


def getENum(s):
    eNum = 0
    nums = "1,2,3,4,5,6,7,8,9".split(',')
    for each in s:
        if each in nums:
            eNum += int(each)
    print(eNum)


getENum(s)
