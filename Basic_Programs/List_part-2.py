# List Part-2

# Packing and Unpacking

# unpacking:-

# l1 = [20,50,30]
# a,b,c = l1
# print(a,b,c)


# packing:-

# a = 5
# b = 6
# c = 10
# l2 = [a,b,c]
# print(l2)


# --------------------------------------------

# Built in method of Lists
# len,min,max,sum,sorted

l1 = [10,3,78,11,2,12]
print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1))
print(sorted(l1))

# sorted function me kuch bhi pass karo(list,tuple) vo sort karete ek new list hi deta hai purane list me koi changes nahi karta hai



# ---------------------------------------------

# list function me iterable type ke argument value hi aa skte hai aur yato ek value dalo ya to khali rahene do jo ek dalenge vo iterable hi hona chiye


# l1 = list()     # li = [] empty list
# l1 = list(10)     # ye galat hai ek argument to diya lekin ye int type ka hai na usko iterable type ka hi chiye
# l1 = list("Sameer")   #ye iterable hai sahi hai ye
# print(l1)
# l2 = list(range(1,6))
# print(l2)



# ---------------------------------------------

# Comparison Operator

# l1 = [1,2,3]
# l2 = [2,3,1]
# l3 = [1,2,3,4,5]
# l4 = [1,2,3]

# print(l1==l2)   #False, same sequence me nahi hai isliye false
# print(l1==l3)   #False, same element to hai kuch extra element bhi hai na
# print(l1==l4)   #True,  same element same sequence me hai
# print(l1>l2)    #False, dono list ke phele phele element compare hoge bs agar l1 ka pehela element bada hua l2 se to True ayega agar l1 ka phele element chota hua l2 se to false



# --------------------------------------------


# Concatination Operation

# l1 = [1,5,9]
# l2 = [2,3,1]
# l3 = l1+l2
# print(l3)


# --------------------------------------------

# Repetition Operator

# l1 = [2,5]
# print(l1*5)

# ---------------------------------------------

# Slicing Operator
# listObject[beg:end:step]
# By default step = 1
# By default beg,end = extreme end

# l1 = [20,40,10,30,60,50]
# print(l1[2:6:2])
# print(l1[4:0:-1])
# print(l1[:])        #starting se end tak
# print(l1[::-1])     #reverse



# agar step ki value positive hoga to to beginning ki value left most end aur end ki value right most end value hogi 

# aur agar step ki value negative hoga to beginning ke case me right most index hoga aur end hoga left most index 