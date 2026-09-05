# Map Reduce and Filter

# Higher order function take function as a parameter and return a function


# map(function,iterable)

# def square(a):
#     return a*a

# x = map(square,[1,2,3,4])
# # x is a map object

# # l1 = list(x)
# # print(l1)

# for e in x:
#     print(e,end=' ')



# ----------------------------------------------

# filter(function,iterable)

# The filter function is used to generate an output list of values that return true when the function is caled

def fun(x):
    if x%2==0:
        return x

# y = filter(fun,(1,2,3,4,5))
# l1 = list(y)
# print(l1)

# ----------------------------------

# t = (10,2,3,0,-4,5,8,19,9)
# y = filter(fun,t)
# print(y)
# for e in y:
#     print(e,end=' ')



# ----------------------------------------------


# reduce(function,iterables)

# The reduce function applies a provided function to iterables and return a single value

from functools import reduce

# x = reduce(lambda a,b: a+b,[1,2,3,4])
# print(x)

# ----------------------------------

def add(a,b):
    return a+b

l1 = [1,2,3,4,5]
x = reduce(add,l1)
print(x)
