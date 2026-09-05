# Decorator: decorator is also a higher order function

# Higher order function takes function as a argument and return a function


def deco_result(result_func):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print(m,"Distinction")
        else:
            result_func(marks) 
    return distinction


@deco_result
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")

marks = [45,18,90,63,54]
result(marks)

# jab jab result function chalega distinction vala function chalega
# decoratior ek function return karega jo function return karega vo chalega
