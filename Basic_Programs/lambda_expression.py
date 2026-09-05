# lambda expression:-

# lambda is a keyword
# through lambda we can create anonymous function
# lambda expression are syntactically restricted to a single expression

# labda input: expression
# lamda a,b : a+b

# no need to def keyword
# lambda automatically returns the value
# lambda function create in that situation when you have to call that function only one time not repetly
# lambda is function object

# l = (lambda a,b : a+b)(2,3)
# print(l)

# l = (lambda a,b : a+b)
# print(l(2,3))


# f = lambda a: 1 if a==0 else a*f(a-1)
# print(f(5))