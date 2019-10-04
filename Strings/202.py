#tag : companies
# Given the values of a, b and x in the equation ax + b = y. Find the value of y.
# Sample Testcase:
# INPUT
# 3 5 2
# OUTPUT
# 11
# done


def equation(a, x, b):
    y = (a*x)+b
    return y


a, b, x = map(int, input().split())
print(equation(a, x, b))
