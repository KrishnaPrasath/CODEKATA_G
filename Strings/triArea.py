# Given base and height of a triangle find the area.
# Input Size: N <= 1000000
# Sample Testcase:
# INPUT
# 2 4
# OUTPUT
# 4
#done
try:
    b, h = map(int, input().split())
except EOFError as e:
    print(0)
print((b*h)*0.5)
