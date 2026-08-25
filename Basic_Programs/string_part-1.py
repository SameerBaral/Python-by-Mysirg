# String

# str is a class
# str is immutable
# str is iterable
# str is hashable
# str is a sequence


# ----------------------------------------------

# Create str object

# s1 = "Sameer"
# s2 = 'Sameer'
# s3 = """Mysirg"""
# s4 = '''Mysirg'''
# s5 = str()  #str empty string object
# s6 = str(125)
# s6 = str(3.45)



# --------------------------------------------
# Accessing str elements

# s1 = 'Mysirg'
# print(s1)
# for e in s1:
#     print(e,end=' ')
# print(s1[1:4:1])    #slicing operator 4 exclude
# print(s1[:4])
# print(s1[::-1])



# ----------------------------------------------
# Builtin method

# s1 = "MySirG"
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sorted(s1))


# ----------------------------------------------

# Concatination and Repetition Operator

# s1 = "ABC"
# s2 = "DE"
# print(s1+s2)


# s1 = "ABC"
# print(s1*3)

# ----------------------------------------------

# Comparision Operator

# s1>s2 => True if s1 comes after s2 in dictionary order

# s1 = "Ramesh"
# s2 = "Rahul"
# print(s1>s2)


# -----------------------------------------

# string methods

# s1 = "mysirg education services"
# print(s1.index("g"))
# print(s1.count("e"))
# print(s1.startswith("my"))
# print(s1.endswith("services"))


# s2 = "Sameer123"
# print(s2.isdigit())
# print(s2.isalpha())
# print(s2.isupper())
# s2 = s2.upper()
# print(s2.isupper())
# s2 = s2.replace("123","456")
# print(s2)