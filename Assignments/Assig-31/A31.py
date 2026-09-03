# Assignment on dict


# Que-01

# d1 = {n:n**2 for n in range(1, int(input("Enter a number: "))+1)}
# print(d1)



# Que-02

# d1 = {n:n**2 for n in range(1, int(input("Enter a number: "))+1)}
# l1 = sorted(d1,reverse=True)
# print(l1)




# Que-03

# n=int(input("How many prayers data you want to store?"))
# players={}
# for i in range(1,n+1):
#     name=input("Enter name of the player")
#     print("Enter number of matches palyed")
#     a=input()
#     print("Total runs")
#     b=input()
#     print("Half Centuries")
#     c=input()
#     print("Centuries")
#     d=input()
#     players[name]=(a,b,c,d)
# for k,v in players.items():
#     print(k,v)




# Que-04

# batches={
#     'SA':200,
#     'SB':189,
#     'SC':207,
#     'SD':305,
#     'SE':280
# }
# max=0
# batch_code=''
# for k,v in batches.items():
#     if(v>max):
#         max=v
#         batch_code=k
# print("Max size batch code is",batch_code)



# Que-05
cities=[
    "Bhopal",
    "Indore",
    "Jabalpur",
    "Ujjain",
    "Gwalior",
    "Bikaner",
    "Jaipur",
    "Pune",
    "Patna",
    "Kanpur",
    "Panjim"
]
d={}
for alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    names=[]
    for city in cities:
        if city.startswith(alpha):
            names.append(city)
    if len(names)>0:
        d[alpha]=names
for k,v in d.items():
    print(k,v)
