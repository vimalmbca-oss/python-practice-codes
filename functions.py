#function
'''
def add():
    a=10
    b=30
    print(a+b)
add()    
'''
#user defined function
#without argument
'''
def add():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a+b)
add()    
'''
#with argument
'''
def add(a,b):
    print(a+b)
a=int(input("enter a:"))
b=int(input("enter b:"))
add(a,b)
'''
#arguments types
#1.positional
'''
def add(a,b,c):
    print(a+b+c)
add(10,20,4)
'''
#2.default
'''
def add(a,b=2):
    print(a+b)
add(10,5)
'''
#3.keywords
'''
def calc(**a):
    for i,j in a.items():
        print(i,j)
calc(a=10,b=20,c=4)
'''
#4.variable
'''
def a(*b):
    for i in b:
        print(i)
a(10,20,"hii")
'''
#lambda function
'''
a=lambda b,c:b*c
print(a(3,4))
'''
#return function
'''
def add(a,b):
    return a+b
print(add(10,20))
'''
#or
'''
def add(a,b):
    return a+b
c=add(10,20)
print(c)
'''
#calculator
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
n1=int(input("enter a:"))
n2=int(input("enter b:"))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
ch=int(input("enter your choice:"))
if ch==1:
    print(add(n1,n2))
elif ch==2:
    print(sub(n1,n2))
elif ch==3:
    print(mul(n1,n2))
elif ch==4:
    print(div(n1,n2))
'''    







































