
# Que-1

# num = int(input("Enter a number: "))
# f = 1
# for i in range(1, num + 1):
#     f = f*i
# print("Factorial of", num, "is", f)




# Que-2

# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print("Number of digits:", count)



# Que-3

# num = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     sum += num % 10
#     num = num // 10
# print("Sum of digits:", sum)




# Que-4

# d = 25
# s = ''
# while d:
#     s = str(d%2)+s
#     d = d//2
# print("Binary representation:", s)




# Que-5

d = 25
s = ''
while d:
    s = str(d%8)+s
    d = d//8
print("Octal representation:", s)