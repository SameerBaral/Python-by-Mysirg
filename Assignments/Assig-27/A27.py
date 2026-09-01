# More on String Assignment

# Que-01

# s1 = input("Enter a string: ")  
# l1 = s1.split(' ')
# l1 = l1[::-1]
# print(' '.join(l1)) 



# Que-02

# s1 = input("Enter a string: ")
# l1 = []
# for word in s1.split(' '):
#     try:
#         l1.append(int(word))
#     except:
#         pass
# print("List of integers:", l1)



# Que-03

# s1 = input("Enter a string: ")
# if s1==s1[::-1]:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")



# Que-04

# s1 = input("Enter a string: ")
# print("String in Uppercase:", s1.upper())



# Que-05

# s1 = input("Enter a string: ")
# i = 0
# index = 0
# maxLength = -1
# for w in s1.split(' '):
#     if maxLength < len(w):
#         maxLength = len(w)
#         index = i
#     i += 1
# print("Max length word:", s1.split(' ')[index],"is",maxLength)
  
