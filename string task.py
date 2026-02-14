#1.reverse a string
'''
y=str(input("enter the string:"))
l=""
for i in y:
    l=i+l
print(l)
'''

#2.find a palindeinr
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
#3.replace a word with a another word

s="PYTHON"
print(s)
print(s.replace('T','O'))

#4.concatenate the two string
'''
a=str(input("enter the string:"))
b=str(input("enter the string:"))
print(f'{a} {b}')
'''
#5.check digits in string
'''
a="12345"
print(a.isdigit())
'''
#6.convert the first letter
'''
n=str(input("enter the word:"))
print(n.title())
'''
#7.count the vowels
'''
string=str(input("enter the string:"))
count_vowels = 0
count_char = 0
for v in string:
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        count_vowels = count_vowels+1
    else:
        count_char = count_char + 1
print("no of vowels in a sentance is:",count_vowels)
print("no of char in a sentance is:",count_char)
'''
#
'''

a=int(input("enter the number:"))
b=0
c=1
t=a
while t>0:
    d=t%10
    b=b+d
    c=c*d
    t=t//10
if b==c:
    print(a,"is a spy number")
else:
    print(a,"is not spy number")

'''
#find special number
'''
a=int(input("enter the number:"))
b=0
c=1
t=a
while t>0:
    d=t%10
    b=b+d
    c=c*d
    t=t//10
    d=b+c
if a==d:
    print(a,"is a special number")
else:
    print(a,"is not special number")
'''
'''
#harshad number
a=int(input("enter the number:"))
b=0
t=a
while t>0:
    d=t%2
    b=b+d
    t=t//2
if b>0:
    print(a,"is a harshad number")
else:
    print(a,"is not harshad number")
'''


y="malayalam"
l=" "
for i in y:
    l=i+l
    a=l
if y==a:
    print(a,"is a palindeiner")
else:
    print(a,"is not a palindeiner")
    
    
