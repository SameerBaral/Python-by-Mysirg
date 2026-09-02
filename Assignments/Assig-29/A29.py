# Tuple Assignments


# Que-01

# l1 = input("Enter a list of elements separated by commas: ").split(',')
# t1 = tuple(l1)
# print(t1)



# Que-02

# t1 = (10,20,30,40,50)
# print(t1[::-1])



# Que-03

# l1 = ['bhopal','patna','pune','bharatpur','jaipur','jodhpur']
# mylist = []
# temp = []
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# l1.sort()

# for i in range(0,26):
#     for j in l1:
#         if j.startswith(alpha[i]):
#             temp.append(j)
#     if len(temp) > 0:
#         mylist.append(tuple(temp))
#         temp.clear()
# print(mylist)




# Que-04

# mylist = []
# for i in range(65,91):
#     mylist.append((chr(i),i))
# print(mylist)



# Que-05

# t1 = (20,30,45,11,23,10,80)
# s = 0
# for i in t1:
#     if i % 2 == 1:
#         s += i
# print("Sum of odd numbers is:",s)