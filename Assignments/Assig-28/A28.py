# list and str mixed Assignment


# Que-1

# l1 = [20,4.5,'abc',True,30,40]
# i=0
# l2 = []
# while i<len(l1):
#     if type(l1[i])==int:
#         l2.append(l1[i])
#     i+=1
# print(l2)




# Que-2 find distinct element frequency from list

# l1 = [20,20,30,40,30,20,40,50,20,40]
# i = 0
# for x in l1:
#     if i==l1.index(x):
#         print(f"{x} : {l1.count(x)}")
#     i+=1




# Que-3 sort list of strigs

# l1 = ["Bhopal","Indore","Jabalpur","Gwalior","Ujjain","Itarasi"]
# l1.sort()
# print(l1)



# Que-4 first repeated string in a list of strings

# l1 = ["AB","BC","BC","AB","BC","CA","CA"]
# i = 0
# for s in l1:
#     if i!=l1.index(s):
#         print(f"First repeated string is : {s}")
#         break
#     i+=1




# Que-5

# l1 = ["Places","Services","white","fly","walk","pastries","royal","games"]
# count = 0
# for s in l1:
#     if s.endswith('s'):
#         count+=1
# print(f"Total string ends with 's' : {count}")