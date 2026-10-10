# Assignment-34      Function part-3


# Que-1

# def oddNaturalNumbers(n):
#     for i in range(1, n + 1):
#         print(2*i-1, end=" ")

# oddNaturalNumbers(10)



# Que-2

# def isPrime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# def nextPrime(num):
#     num+=1
#     while(not isPrime(num)):
#         num+=1
#     return num
# def printPrime(n):
#     x=2
#     for i in range(1,n+1):
#         print(x,end=' ')
#         x=nextPrime(x)

# printPrime(10)



# Que-3

# def printPrimeRange(a,b):
#     x=a+1
#     while x<b:
#         if isPrime(x):
#             print(x,end=' ')
#         x+=1




# Que-4 | -1 1 0 1 1 2 3 5 8 13 21 34 55 89 ...

# def printFib(n):
#     a,b=-1,1
#     while(n):
#         c=a+b
#         print(c,end=' ')
#         a,b=b,c
#         n-=1

# printFib(10)



# Que-5 | 36 = 1,2,3,4,6,9,12,18,36

# def printFactors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=' ')
# printFactors(36)