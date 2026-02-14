#while loop increment
'''
i=1
while i<=5:
    print(i)
    i=i+1
'''
'''
i=int(input("enter the number:"))
while i<=5:
    print(i)
    i=i+1
'''
'''
i=1
while i<=5:
    print(i)
    i=i+2
'''    
#while loop decrement
'''
i=5
while i>=1:
    print(i)
    i-=1
'''
'''
i=5
while i>=1:
    print(i)
    i=i-2
'''
'''
i=int(input("enter the number:"))
while i>=1:
    print(i)
    i=i-1
'''
#infinity loop
'''
while true:
    print(1)
'''
'''
i=1
while i<=5:
    print(i)
    i=i-1
'''
'''
i=5
while i<=5:
    print(i)
    i=i-1
'''    
#transfer and jumping statement
#break
'''
for i in range(5):
    if i==5:
        break
    else:
        print(i)
'''
'''
#continue
for i in range(10):
    if i==6:
        continue
    else:
        print(i)
'''
'''
#pass
for i in range(5):
    if true :
        pass
    else:
        print("hello")
'''
#palindeiner
'''
a=121
b=0
t=a
while t>0:
    d=t%10
    b=b*10+d
    t=t//10
if b==a:
    print(b,"is a palindeiner")
else:
    print(b,"is not a palindeiner")
'''
'''
a=int(input("enter the number:"))
b=0
t=a
while t>0:
    d=t%10
    b=b*10+d
    t=t//10
if b==a:
    print(b,"is a palindeiner")
else:
    print(b,"is not a palindeiner")
'''
#amrsstrong
'''
a=153
b=0
t=a
while t>0:
    d=t%10
    b=b+d**3
    t=t//10
if b==a:
    print(b,"is a amrsstrong")
else:
    print(b,"is not a amrsstrong")
'''
'''
a=int(input("enter the number:"))
l=int(len(str(a)))
b=0
t=a
while t>0:
    d=t%10
    b=b+d**l
    t=t//10
if b==a:
    print(b,"is a amrsstrong")
else:
    print(b,"is not a amrsstrong")
'''

