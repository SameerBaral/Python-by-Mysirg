# iterable:  group of elements

#------------ range --------------------------

# range is a class
# range is immutable sequence
# range can contain only int type values
# range contains sequence of integers with common defference(Arithmetic progression)
# range elements are indexed

# create range object
# r = range(beginning,end,step)
# beg- inclusive, end- exclusive, step- common gap

#Ex- range(1,10,1)



# ---------------------------------------------

# r1 = range(2,10,3)
# for i in r1:
#     print(i)



# agar range me sirf ek hi value doge to vo end value mana jaega aur beg=0,step=1 bydefault mana jaega

# r1 = range(3)
# for i in r1:
#     print(i)



# agar range me sirf do hi value doge to vo beg,end value mana jaega aur step=1 bydefault mana jaega

# r1 = range(1,4)
# for i in r1:
#     print(i)


# jab bhi aisa galat range dete starting 4 and end=1 aur step 1 to ye 1 tak kabhi pahuchega hi nahi to ye galat range hai ye banega empty range 

# r1 = range(4,1)
# print(r1[0])


# ----------------------------------------------

# positive and negative dono hota isme sbse last element ka index -1 hota fir badhte hue chale ao starting tak

# r1 = range(1,6,1)
# print(r1[4])
# print(r1[-1])


# accessing range element

# r1 = range(10,80,8)

# for e in r1:
#     print(e,end=' ')

# accessing through while loop

# i = 0
# while i<9:
#     print(r1[i],end=' ')
#     i+=1



# ----------------------------------------------

# WAP  to print first n natural numbers using range and for


# n = int(input("Enter a number:"))
# r1 = range(1,n+1,1)
# for i in r1:
#     print(i,end=' ')



# ----------------------------------------------

# WAP to print squares of first n natural numbers using range and for


# n = int(input("Enter a number:"))
# r1 = range(1,n+1,1)
# for i in r1:
#     print(i**2,end=' ')


# ----------------------------------------------

# WAP to print first n even natural numbers in reverse order using range and for

# n=5 ,  10 8 6 4 2

# n = int(input("Enter a number:"))
# r1 = range(2*n,1,-2)
# for i in r1:
#     print(i,end=' ')


# ----------------------------------------------

# WAP to calculate sum of first n multiples of x use range and for.


# n = int(input("Enter a number of multiple:"))
# x = int(input("Enter a number:"))
# s = 0
# r1 = range(1,n+1,1)
# for i in r1:
#     s = s+x*i
# print("Sum is:",s)    
