# string part-2


# format:-

# syntax:=> string.format(var1,var2,...)

# print("{},how are you?".format("Sameer"))
# print("{},{},{}".format("One",25,5.7))
# print("{2},{0},{1}".format(10,20,30))


# ------------------------------------------------

# split and join

# Split-> split function returns a list of splitted strings

# s1 = 'Mysirg Education Services'
# l1 = s1.split(' ')
# print(l1)


# s1 = "10,30,20,50,40"
# l1 = s1.split(',')
# l2 = [int(e) for e in l1]
# print(l2)


# s1 = input("Enter integers separated by comma: ")
# l1 = s1.split(',')
# mylist = [int(e) for e in l1]
# print(l1)
# print(mylist)



# ------------------------------------------------

# split()=> str-->          list of str
# jion()=>  list of str-->  str

# join

# join isko list of str denge ye return katra hai single string

# l1 = ["25","12","2022"]  #list of string
# l2 = "-".join(l1)   #list return single string
# print(l2)
