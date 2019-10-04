# Given a sentence interchange the words around the word 'and'.
# Input Size: | S | <= 1000000
# Sample Testcase:
# INPUT
# jack and jill went up and down to get water
# OUTPUT
# jill and jack went down and up to get water
# done

s = list(map(str, input().split(' ')))

for i in range(len(s)):
    if s[i] == 'and':
        temp = s[i-1]
        s[i-1] = s[i+1]
        s[i+1] = temp

print(*s)
