# Write a program which displays whether the given two strings are complementary or not.
# Assume both the string contains unique capital alphabets in alphabetical order.
# Their total length has to be 26. If we join alphabets of both the strings we should get
# all capital letters exactly once, then only we can call them as complementary.
# Print complementary/non-complementary.
# Sample Testcase:
# INPUT
# ABDCFGIJKLMNOPQUVWXYZ
# EHRST
# OUTPUT
# complementary
#check with JOHN


A = input()
B = input()

C = A + B

dic = {}

for each in C:
    dic[each] = 0

# if(object.keys(dic).length)
if len(dic) == 26:
    print('complementary')
else:
    print('non-complementary')
