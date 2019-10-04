# N = int(input())
# count = 1
# for i in range(N):
#     for j in range(count):
#         print(1, end='')
#     if(i < N-1):
#         print()
#     count += 2

# done

N = int(input())
count = 1
for i in range(N):
    for j in range(count):
        if j < count-1:
            print(1, end=' ')
        else:
            print(1)
    count += 2
