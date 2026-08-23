# dictionary


# dict is a class
# dict is mutable
# dict is not hashable
# dict is iterable
# dict is not a sequence
# dict cannot have duplicate keys(not data values)
# indexing is not applicable to dict object
# slicing operator is not applicable
# dict elements are pair of key-value and data-value
# one dict element is (key,data)
# kye kisi bhi type ka ho skta hai

# -------------------------------------------------

# How to create dict object:-

# d1 = {101:'Rahul',103:'Payal',104:'Arjun',105:'Prachi'}
# print(d1)

# d1 = {}     #empty object
# print(d1)

# d1 = dict(a=10,b=20,c=30)
# print(d1)


# Accessing dict elements:-

d1 = {101:'Rahul',103:'Payal',104:'Arjun',105:'Prachi'}
# print(d1[101])   # Rahul

# har key ko access karne ke liye for loop ka use kr skte hai
# for k in d1:
#     print(k,d1[k])   # Rahul,Payal,Arjun,Prachi


# edit dict elements:-
# d1[102] = 'Sneha'
# print(d1)


# dict class functions:-ye sb iterable hote hai

print(d1.items())
print(d1.keys())
print(d1.values())