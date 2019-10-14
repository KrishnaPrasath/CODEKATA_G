# Write a program to calculate the total surface area and volume of cuboid. Input contains
#  three space separated positive integers L, B, H denoting the length, width and height of cuboid respectively.
# Sample Testcase :
# INPUT
# 1 2 3
# OUTPUT
# 22 6

#done 30c

# Cuboid
# Surface
# S = 2(ab+ac+bc)
# Volume
# V = abc
# Diagonal
# e = √(a2+b2+c2)

L,B,H = map(int,input().split())

def surface (a,b,c):
    return 2*(a*b+a*c+b*c)
def volume(a,b,c):
    return a*b*c

print(surface(L,B,H),volume(L,B,H))