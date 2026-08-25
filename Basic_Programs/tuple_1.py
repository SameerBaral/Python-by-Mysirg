# Tuple 

# tuple is class
# tuple is iterable
# tuple is immutable
# tuple is hashable
# tuple is a sequence


# -----------------------------------------------

# t1 = (12,33,44,67)
# print(t1)

# t2 = ()    #empty tuple
# print(t2)

# tuple ke andar agar ek hi element hoga to vo tuple type ka nahi int type ka ho jaega 
# t3 = (20)
# print(type(t3))

# single element rakhna hai tuple type ka ho to single element ke bad comma laga do
# t4 = (10,)
# print(type(t4))

# perenthisis () agar na lagaye aise hi likhde to bhi bydefault tuple khelayega
# t5 = 10,30,40,60,70
# print(type(t5))


# -----------------------------------------------

# t1 = (14,59,70,12,3,50,60,90,77)
# print(t1[2:8:2])


# Accessing tuple elements:-

# t1 = (10,5,20,15)
# print(t1[1])


# t1 = (10,5,20,15)
# i = 0
# while (i<len(t1)):
#     print(t1[i],end=' ')
#     i+=1


# t1 = (10,5,20,15)
# for e in t1:
#     print(e,end=' ')



# ------------------------------------------------

# concatination and repetition operation

# t1 = (10,20)
# t2 = (11,22,33)
# print(t1+t2)
# print(t1*2)


# ------------------------------------------------

# comparisioon operator

# t1 = (10,20)
# t2 = (11,22,33)
# print(t1>t2)    #sirf phela num se compare karta h
# print(t1==t2)


# ------------------------------------------------

# tuple object methods
# index(): it returns perticular element first occurance index

# t1 = (10,8,53,72,2,8)
# print(t1.index(8))


# count:

# t1 = (10,8,53,72,2,8)
# print(t1.count(8))


# ------------------------------------------------
# taking user input and converting it into tuple

# t1 = tuple([1,2,3,8])
# print(type(t1))

# t1 = tuple([int(e) for e in input("Enter numbers: ").split(',')])
# print(t1)


