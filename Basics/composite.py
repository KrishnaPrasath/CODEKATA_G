# # Given a number N, print 'yes' if it is composite else print 'no'.
# # Sample Testcase :
# # INPUT
# # 123
# # OUTPUT
# # yes

N = int(input())


def checkComposite(N):
    if N <= 3:
        print('no')
        return
    while True:
        for i in range(2, N):
            for j in range(2, N):
                if i * j == N:
                    print("yes")
                    return
        else:
            print("no")
            return


checkComposite(N)

# print(composite)
# # print(prime)
###################################
# N = int(input())
# def checkComposite(N):
# 	if(N<=3):
#         print('no')
#         return


#     while True:
#         for i in range(2, N):
#             for j in range(2, N):
#                 if i * j == N:
#                     print("yes")
#                     return
#         else:
#             print("no")
#             return

# checkComposite(N)
