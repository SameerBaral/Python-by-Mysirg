# Assignment-13


# Que-1 

# num = int(input("Enter a number:"))
# if num>99 and num<1000:
#     print("Three digits number")
# else:
#     print("Not a Three digits number")


# ---------------------------------------------


# Que-2

# num = int(input("Enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")


# ----------------------------------------------

# Que-3


# print("Enter values of a ,b and c:")
# a,b,c = int(input()),int(input()),int(input())
# d = b**2-4*a*c
# if d>0:
#     print("Real and distinct roots")
# elif d==0:
#     print("Real and equal roots")
# else:
#     print("Imaginary roots")



# --------------------------------------------


# Que-4

# 4 se divisible vale to hote leap year 
# sare century year leap year nahi hote hai, har century year divide to hote hai 4 se


# year = int(input("Enter a year:"))
# if year%100==0:
#     if year%400==0:
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     if year%4==0:
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")



# ----------------------------------------------


# Que-5

print("Enter three numbers:")
a,b,c = int(input()),int(input()),int(input()) 
if a>b and a>c:
    print("Greater no. is:",a)
elif b>c:
    print("Greater no. is:",b)
else:
    print("Greater no. is:",c)
