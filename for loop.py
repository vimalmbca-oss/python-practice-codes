'''
#for loop using integer
for i in range(1,6,1):
    print(i)
'''
'''
#nested for loop
n=5
for i in range(n):
    for j in range(i+1):
        print(j,end="")
    print()
'''
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
'''
'''
# 1.factorial of numbers
f=1
for i in range(1,6):
    f=f*i
print(f)
'''
'''
#natural number
for i in range(1,11,1):
    print(i)
'''
'''
#inverted half pramid
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()    
'''
'''

#full pramif
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(j,end=" ")
    for j in range(i):
        print(j,end=" ")    
    print()
'''                                                       

'''
n=5
for i in range(n):
    for j in range(i,n):
        print(i,end="")
    print()
'''

'''
#sum of natural number
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
'''

''''
#multiplication number
n=int(input("enter the number:"))
for i in range(1,11):
    table = i * n
    print(n, "*" ,i, "=" ,table)
print()
'''
'''
#odd or even
sum=0
for i in range(1,11):
    sum=sum+i
if sum%2==0:
    print(sum,"is an odd n")
else:
    print(sum,"is an even n")
'''
'''
#tirangle
n=5
for i in range(n):
    for j in range(i+1):
        print("2",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i,n):
        print("3",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
'''    
#full pramif
n=5
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()
                 
































