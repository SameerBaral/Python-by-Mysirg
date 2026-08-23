# print() function


# print("Welcome")

x=10
# print(x)

# print(x+5*3)

y=20
# print(x,y)      #ye value bydefault seperate hoti hai space se


# we can also change seperator value

# print(x,y,sep='-')
# print(x,y,sep='##')



a=5
b=10
c=15

print(a,b,c)
print("Sameer")     #bydefault print new line leta hai



# end  => ye end ko new line jo bydefault raheta usse change kar dega

# print(a,b,c,end=',')
# print("Sameer") 


# sep and end dono ka ek saath use bhi kar skte ho

print(a,b,c,sep='-',end='!')
print("Sameer") 



# Special Characters
# Escape sequences

# print("Hello\nStudents")        #new line
# print("Hello\tStudents")        #tab space
# print("Hello\bStudents")        #back space

# print("Hello\rStudents")        #carriage return
# print("Sameer\rBaral")        #carriage return





# Formate specifier

x=4
print("value of x is",x)
print("value of x is %d"%(x))

