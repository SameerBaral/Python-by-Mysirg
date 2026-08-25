# Positional Arguments:-


# def f1(a, b):   # formal arguments
#     print("a:", a)
#     print("b:", b)

# f1(10, 20)  # actual arguments



# -----------------------------------------------


# Keyword Arguments:-

def f2(a, b):   # formal arguments
    print("a:", a)
    print("b:", b)

# f2(b=1,a=3) # actual arguments
# f2(2,a=3) # runtime error a got multiple values
# f2(2,b=3) # no problem
# f2(b=3,2) # ye compiletime error hai, you cannot have positional argument after keyword argument
