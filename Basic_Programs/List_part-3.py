
# list inside list:-

# l1 = [[1,3,5],[2,1,8],[5,4,4]]
# print(l1[1])
# print(l1[1][2])


# ----------------------------------------
# Exploring list various methods:-


# remove: vo element dedo jo hatana ho ye first occurance ko hi remove karta hai bs

# l2 = [50,80,20,10,67,80,12]
# l2.remove(80)     
# print(l2)

# -----------------------------------------
# del keyword se bhi delete kar skte bs index pss kana hoga

# l3 = [50,20,10,67,80,12]
# del l3[2]
# print(l3)


# ------------------------------------------
# pop() : remove element from the last one at a time
# pop last element return bhi karta hai jisko hataya hoga

# l4 = [50,80,20,10,67,80,12]
# l4.pop()
# print(l4)

# l4.pop(3)
# print(l4)

# remove all element from the list
# l4.clear()  
# print(l4)


# l4.reverse()
# print(l4)

# l4.sort()
# print(l4)


# print(l4.index(10))

# ------------------------------------------


# list comprehension:-

# for loop ke body me agar ek hi line hoga tab iskaistemaal karte hai, for ke body vala part hi ata hai for keyword ke phele

# [print(x**2+1) for x in range(1,6)]


# ----------------------------------------

# Taking input string ke har element ko list ka ek ek element bana dega

# aise list ka input nahi lenge bcz har cheez string ja raha string ka har ek element fir list me convert ho raha
# l5 = list(input())
# print(l5)

# -----------------------------

print("How many numbers you want to enter:")
n = int(input())
l1 = []
i = 0
while i<n:
    l1.append(int(input("Enter a number:")))
    i+=1
print(l1)