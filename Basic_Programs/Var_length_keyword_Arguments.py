# Var length keyword Arguments

# * single me tuple banta hai
# ** double me dict object banta hai key value ka pair


# keyword length argument:-

# def personinfo(**kwargs):
#     for k,v in kwargs.items():
#         print(k,'-',v)

# personinfo(name="Sameer",age=22)
# personinfo(name="Ajay",age=22,mark=50)
# personinfo(name="Rahul",empid=121,age=22)

# -----------------------------

def f2(**d):
    for k,v in d.items():
        print(k,'-',v)

d1 = {'a':2,'b':4,'c':6}
f2(**d1)


# non keyword argument:-

# def f1(*t):
#     print(t)
# f1(10,20,30)

# --------------------------

# def f1(*t):
#     print(t)
# t1 = (5,10,15,20)
# f1(*t1)
