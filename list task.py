#sum of two list
'''
a=[1,2,3,4]
b=[5,6,7,8]
sum=a+b
print(sum)
'''
#find largest number
'''
a=[12,20,35,50]
print(max(a))
'''
#find smallest number
'''
a=[12,20,35,50]
print(min(a))
'''
#find the dulpicate value
'''
a=[1,2,3,1,2,3,4]
b=(set(a))
print(b)
'''
#copy the list
'''
a=[1,2,3,1,2,3,4]
b=a.copy()
print(b)
'''
#reverse the list
'''
a=[12,20,35,50]
a.reverse()
print(a)
'''
#crete a list with random value
'''
a=[]
a.extend((200,300,400))
print(a)
'''
#remove empty element
'''
a=[1,2,3,4,5]
a.clear()
print(a)
'''
#append the value to list
'''
a=[1,2,3,4]
b=[5,6,7,8]
b.append(a)
print(b)
'''
#choose the random items
'''
import random
a=[30,20,10]
b=random.choice(a)
print(b)
'''
#add and even
'''
B=[11,30,45,23,45]
even=[]
odd=[]
for i in B:
    if i%2==0:
        even.append(B)
        print("even numbers",even)
    else:   
        odd.append(B)
        print("odd number",odd

                number in ascending order

a=[1,2,4,5,7,3,8,9]
a.sort()
print(a)
    
    
