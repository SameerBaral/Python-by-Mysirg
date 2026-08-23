# Transfer Control Statement

# break,continue,else with loop,pass


#break

# i = 1
# while i<=10:
#     print(i,end=' ')
#     a = int(input("Enter a negative number:"))
#     if a<0:
#         break
#     i+=1



# ------------------------------------------------

# i = 1
# while i<=3:
#     num = int(input("Enter an even number:"))
#     if num%2==0:
#         break
#     i+=1
 
# # pora loop chal gya even number nahi dal paye to lose hua
# if i==4:    
#     print("lost the game")
# else:
#     print("Won the game")




# -----------------------------------------------

# Continue
# even no. par koi changes nahi ho raha i ka

# i = 1
# while i<=10:
#     x = int(input("Enter a number:"))
#     if x%2==0:
#         continue
#     print(i,"x=",x)
#     i+=1




# -----------------------------------------------


# else with while loop


# i = 1
# while i<=3:
#     num = int(input("Enter an even number:"))
#     if num%2==0:
#         print("Won the game")
#         break
#     i+=1

# # pora loop chal gya even number nahi dal paye to lose hua  
# else:
#     print("lost the game")




# ------------------------------------------------

# pass iska use wha karna jab apko curly bracket me kuch na likhna ho while if loop me uske body me kuch nahi likhna ho tab pass likh skte

# if 1<5:
#     pass
# print("Hello")