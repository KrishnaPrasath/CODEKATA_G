# Given a number 'N' print the sum of each digit to the power of number of digits in given input.
# Example :
# Input => 1234
# => ( 1 ^ 4 ) + ( 2 ^ 4 ) + ( 3 ^ 4 ) + ( 4 ^ 4 )
# => 1 + 16 + 81 + 256
# Output => 354
# N <=100000000000
# Sample Testcase :
# INPUT
# 1234
# OUTPUT
# 354
# done
N = int(input())
count = 0
digits = []


def countDigits(N):
    count = 0
    while N > 0:
        digits.append(N % 10)
        count += 1
        N = N//10
    return count


count = countDigits(N)

# for each in digits:
result = [i**count for i in digits]

print(sum(result))
