# Assignment on Set


# Que-01

# l1 = [10,20,30,20,30,10,40]
# for i in set(l1):
#     print(i)  




# Que-02

# s1 = {10,12,49,70,53,40,21,16} 
# odd = set()
# even = set()

# for i in s1:
#     if i%2==0:
#         even.add(i)
#     else:
#         odd.add(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)




# Que-03

# s1 = {"Virat","Sachin","Rohit","Hardik","Kapil"}
# i = 0
# for p1 in s1:
#     i+=1
#     for p2 in list(s1)[i::]:
#         print(p1,"and",p2)




# Que-04

# candidates={"Arjun","Atishay","Priyam","Pankaj","Harish",
# "Amit","Sohail","Rahul","Deepak","Rajesh","Gurpreet"}
# black_hat_candidates={"Priyam","Deepak","Harish","Amit","Rahul","Rajesh"}
# red_shoes_candidates={"Arjun","Pankaj","Priyam","Rahul","Gurpreet"}
# s1=black_hat_candidates.intersection(red_shoes_candidates)
# for c in s1:
#     print(c)




# Que-05

# n=int(input("Enter sum of dice numbers "))
# s1=set()
# for i in range(1,7):
#     for j in range(1,7):
#         if i+j==n:
#             s1.add((i,j))
# print(s1)

