import sys


A = map(int, raw_input().strip().split(" "))
B = map(int, raw_input().strip().split(" "))
# print a, b

# counta,countb = 0,0
# for i in range(len(a)):
#     if a[i] > b[i]:
#         counta+=1
#     if a[i] < b[i]:
#         countb+=1
# print counta, countb

# print sum(1 for i in range(len(A)) if A[i]>B[i]), sum(1 for i in range(len(B)) if B[i]>A[i])

print sum(1 for a, b in zip(A, B) if a>b), sum(1 for a, b in zip(A, B) if b>a)