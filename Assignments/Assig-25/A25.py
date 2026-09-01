
# Que-1 Create a list of first N even numbers 

# num = int(input("Enter a number: "))
# l1 = list(range(2,2*num+1,2))
# print("List of even numbers:", num, ":", l1)




# Que-2 Create a list of first N terms of fibbonacci series
# 0 1 1 2 3 5 ...

# n = int(input("Enter a number: "))
# a,b = -1, 1
# l2 = []
# while n:
#     c = a+b
#     l2.append(c)
#     a = b
#     b = c
#     n-=1
# print("List of first N terms of fibbonacci series:", l2)




# Que-3 Create a list of first N prime numbers

# n = int(input("Enter a number: "))
# l3 = []
# x = 2
# while n:
#     for i in range(2,x):
#         if x%i == 0:
#             break
#     else:
#         l3.append(x)
#         n-=1
#     x+=1
# print("List of first N prime numbers:", l3)




# Que-4 Add two matrices of order 3x3

# print("Enter 9 elements of first matrix (row wise):")
# A = [
#     [int(s) for s in input().split(',')],
#     [int(s) for s in input().split(',')],
#     [int(s) for s in input().split(',')]
# ]
# print("Enter 9 elements of second matrix (row wise):")
# B = [
#     [int(s) for s in input().split(',')],
#     [int(s) for s in input().split(',')],
#     [int(s) for s in input().split(',')]
# ]

# c = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0,3):
#     for j in range(0,3):
#         c[i][j] = A[i][j]+B[i][j]
#         print(c[i][j], end = " ")
#     print()




# Que-5 Separate a list into two lists positive and non positive numbers

num = [12,-22,34,66,11,-2,-5,11,-10]
positive = []
negative = []
for e in num:
    if e>0:
        positive.append(e)
    else:
        negative.append(e)
print(positive,negative)