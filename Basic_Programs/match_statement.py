
# match statement switch case jaisa hota python me bs break nahi lagta beech me

x = int(input("Enter a number:"))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("Invalid Value")