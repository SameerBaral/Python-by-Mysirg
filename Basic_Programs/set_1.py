# Set :-


# set is a class
# set is mutable
# set is not hashable
# set is iterable
# set is not a sequence
# set cannot have duplicate values
# indexing is not applicable to set object
# slicing operator is not applicable
# set does not guarantee to store values in the order of insertion



# -----------------------------------------------


# s1 = {10,20,30,40,50}
# print(type(s1))
# print(s1)


# if you take duplicate value then only single value hi store hoge
# s1 = {10,20,30,10,40}
# print(s1)


# aise empty set object nahi banega dict ka object ban jaega 
# s1 = {}
# print(type(s1))


# set class ka object banane ke liye 
# s1 = set()
# print(type(s1))


# set function me ek se jyada argument nahi pass kar skte hai
# s1 = set(10,20,30)   #error


# single value jo pass karege vo iterable type ka hi hona chiye
# s1 = set(10)      #Error not a iterable type


# s1 = set([11,12,13])
# print(s1)

# s1 = set('mysirg')
# print(s1)



# ----------------------------------------------

# Accessing set elements:-


# s1 = {10,20,30,40,50}
# for i in s1:
#     print(i,end=" ")


# sorted function ek list hi return karta hai
# s1 = {25,36,12,73,10}
# sort1 = sorted(s1)
# print(sort1)


#Note: elements of set object must be hashable

# s1 = {10,[1,2,3],2+3j,(2,3),range(6)}
# print(s1)


# ----------------------------------------------

# Comparision Operator:-

# s1 = {1,2,3}
# s2 = {3,2,1}
# print(s1==s2)

# s3={5,4}
# print(s1>s3)


# -----------------------------------------------

# s1 = {1,2,3}
# s1.add(4)
# print(s1)

# s1.add('abc')
# print(s1)

# s1.add((12,33))
# print(s1)

# s1.discard(2)
# print(s1)

# s1.remove(2)
# print(s1)

# update: this function can only take iterable object
# s1.update([10,20,88])
# print(s1)


# ----------------------------------------------
# set comprihension:

# s = {e**2 for e in range(1,6)}
# print(s,end=" ")


# ------------------------------------------

# union operation:- sare element

# s1 = {1,2,4}
# s2 = {5,7,2}

# s3 = s1.union(s2)
# print(s3)


# intersection operation:- common element

# s4 = s1.intersection(s2)
# print(s4)



# s = input("Enter a string:")
# s1 = set()
# for i in s:
#     if i in "aeiouAEIOU":
#         s1.add(i)
# print("Vowels in the string are:",s1)


# set is a mutable object while frozenset provide immutable implementation