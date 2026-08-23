# List Part-1

# List is a class
# List is an iterabe sequence
# List is mutable
# List is growable
# List can store heterogeneous data
# List elements are indexed



# ----------------------------------------------

# Create List object

# l1 = [10,20,30,40]
# l2 = []               #empty list object
# l3 = [20,2.4,"abc"]   #heterogeneous elements


# accessing list objects

# l1 = [10,20,30,40,50]
# print(l1)
# print(l1[0])
# print(l1[1],l1[2])
# print(l1[-1])

# ------------------------------------------------

# Accessing list elemets via for loop

# l1 = [50,20,80,10,60,40]
# for x in l1:
#     print(x,end=' ')


# i=0
# while i<=5:
#     print(l1[i],end=' ')
#     i+=1


# -----------------------------------------------
# delete an element from the list

# l1 = [10,20,30,40,50]
# del l1[2]
# print(l1)
# print(l1[2])


# edit an element of the list

# l1 = [50,20,80,10,60,40]
# l1[2] = 45
# print(l1)


# ----------------------------------------------

# Add more elements in list

#add element end of the list
# l1 = [10,20,30,40]
# l1.append(50)    
# print(l1)

# insert()- ye insert karega element given index me
# l1 = [10,20,30,50]
# l1.insert(3,40)
# print(l1)

# insert function me agar last index se jyada bada index dedoge to error nahi ayega vo last index ke baad me append ho jata hai
# l1.insert(12,100)
# print(l1)