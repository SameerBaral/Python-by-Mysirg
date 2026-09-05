# Assignment on Functions-2 (TSRS)


# Que-01

# def checkeven(num):
#     if num%2==0:
#         return "Even"

# print("The number is:", checkeven(10))



# Que-02

# def greter(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>c:
#             return b
#         else:
#             return c

# print("The greter number is:", greter(12,34,30))




# Que-03

# def isPrime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True

# print("The number is prime:", isPrime(11))




# Que-04

# def isLeapYear(year):
#     if year%100==0:
#         if year%400==0:
#             return True
#         else:
#             return False
#     else:
#         if year%4==0:
#             return True
#         else:
#             return False

# print("The year is leap year:", isLeapYear(2020))




# Que-05

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact

# print('factorial of the number is:', factorial(5))