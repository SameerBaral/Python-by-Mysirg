# Exception Handling:-

# a = int(input("Enter a number:"))
# print(a)

# l1 = [1,2,3,8]   #IndexError
# print(l1[5])


# --------------------------------------

# Handle exception:-
# agar hum exception handel karte hai try block se to preference hamare code ko diya jaega ki hamare code ka exception handel code chale agar hum excption nhi karyte hai to python ke default exception handle chalta use case me

#Note:-
# try ke baad yato except ayega yato to finally dono me se koi ek bhi rakh skte ho agar dono likhna ho to phele except fir finally ayega 

# aur except ke agee vo classname likhte jis type ke exception ane ke chances hote hai try block se vo yha except me catch karke appropriate jo kaam kara na ya msg dena de denge

# try ke saath multiple except aa skte lekin finally ek hi bar aa skta hai


# pyhon ka default exception chlne pr errormsg deke turant end kar deta hai program isi liye hum exception handling karte hai

# jsie example ke liye humne except me ValueRrror class likha except ke agee aur agar iska exception nahi aya koi aur ka object bana jaise ZeroDivisionError aur isko agar humne define nahi kare except me tb is case me python default exception handler hal jaega

# default except clause ko sbhi except ke baad me hi likhte ye isliye hota ki itne sare except hum likhe usme bhi koi asia exception choot gya jisko handle na kara ho humne to ye handle karega usko

# syntax:  except:


# ---------------------------------------------

# try:
#     a = int(input("Enter a number:"))
#     print(a)
# except ZeroDivisionError as e:
#     print("Divde by zero is not valid")
# except ValueError as e:
#     print("Entererd value is not a number")
# finally:
#     print("Finally")
# print("Hello")


# python ka default exception handler agar chal jaega to program end ho jega age

# finally to har haal me chalta hi hai


# -----------------------------------

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    c=a/b
    print("Result:",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Some Exception")
else:
    print("No Exception")
finally:
    print("I am going to run in all situations")
print("Some other code")

