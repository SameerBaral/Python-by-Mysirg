# you can define __init__() method in the class (that is, it is optional)
#Simlar to the concept of constructor in c++ or java
# __init__() method invokes implicitly eveerytime when an instance object is created.
# Therefore, __init__() method is the first mthod runs for an object, just after the object creation.


# class Test:
#     def __init__(self):
#         print('Hello')

# t1 = Test()
# t2 = Test()
# t3 = Test()


# -------------------------------------

class Test:
    def __init__(self):
        a = 5 #local variable
        self.a = 4 #instance object variable

t1 = Test()