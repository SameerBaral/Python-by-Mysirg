# Assignment-14


# Que-1

# x = int(input("Enter a number:"))
# match x:
#     case x if 1000>x>99:
#         print("Three digit number")
#     case x:
#         print("Not a three digit number")


# ---------------------------------------------

# Que-2

# num = int(input("Enter a number:"))
# match num:
#     case num if num>0:
#         print("positive")
#     case num if num<0:
#         print("negative")
#     case num if num==0:
#         print("zero")



# ---------------------------------------------


# Que-3

# print("1. Odd Even")
# print("2. Positive and Non Positive")
# print("3. Simple Interest")
# print("4. Roots of Quadratic Equation")

# x = int(input("Enter your choice:"))
# match x:
#     case 1:
#         print("Enter a number:")
#         n = int(input())
#         print("Even" if n%2==0 else "Odd")
#     case 2:
#         print("Enter a number:")
#         n = int(input())
#         print("Positive" if n>0 else "Non-Positive")
#     case 3:
#         print("Enter principle,rate and time:")
#         p,r,t = float(input()),float(input()),float(input())
#         si=p*r*t/100
#         print("Simple interest is:",si)
#     case 4:
#         print("Enter value of a,b and c:")
#         a,b,c = int(input()),int(input()),int(input())
#         r1=(-b+(b*b-4*a*c)**0.5)/2*a
#         r2=(-b-(b*b-4*a*c)**0.5)/2*a
#         print("Roots are:",r1,"and",r2)
#     case _:
#         print("Invalid Choice")




# -------------------------------------------


# Que-4

# # jab data ka type na pata ho kis type ka data ayega to wha eval laga skte hai

# x = eval(input("Enter some data:"))
# match x:
#     case x if type(x)==int:
#         print("Monday")
#     case x if type(x)==float:
#         print("Tuesday")
#     case x if type(x)==complex:
#         print("Wednesday")
#     case x if type(x)==bool:
#         print("Thursday")



# ---------------------------------------------


# Que-5


x = input("Enter a string:")
match x:
    case x if x in "mysirg":
        print("One")
    case x if x in "education":
        print("Two")
    case x if x in "services":
        print("Three")