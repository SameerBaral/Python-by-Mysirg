# String Assignment:- 

# Que-1

# s1 = input("Enter a string: ")
# print(s1.isalpha())

# or

# s1 = input("Enter a string: ")
# for i in s1:
#     if i>='a' and i<='z' or i>='A' and i<='Z':
#         pass
#     else:
#         print("String has atleast one character which is not an alphabet")
#         break
# else:
#     print("String contains only alphabets")



# Que-02

# s1 = input("Enter a string: ")
# ch = input("Enter a character: ")

# if ch in s1:
#     print("%s is in %s" % (ch, s1))
# else:
#     print("%s is not in %s" % (ch, s1))



# Que-03

# s1 = input("Enter a string: ")
# count=0
# for i in s1:
#     if i in 'aeiouAEIOU':
#         count+=1
# print("Vowel count:", count)



# Que-04

# s1 = input("Enter a string: ")
# s1=s1.strip()     #through this we can remove the leading and trailing spaces from the string
# l1 = s1.split(' ')
# print(l1)
# i = 0
# wordCount = 0
# while i < len(l1):
#     if l1[i] != '':
#         wordCount += 1
#     i += 1
# print("Total Words:", wordCount)




# Que-5

# s1 = input("Enter a string: ")
# print(s1[::-1])