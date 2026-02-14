#strings
#indexing
'''
a="hello PYTHON"
print(a)
print(a[8])
print(a[11])
print(a[-4])
print(a[-8])
'''
#string slicing
'''
print(a[6:12])
print(a[6:])
print(a[0:5])
print(a[-12:-7])
print(a[-9:-3])
'''
#reverse string
'''
a="123"
print(a[::-1])
'''


#string build function
'''
a="hello PYTHON"
print(a)
print(a.upper())
print(a.lower())
print('i am python'.capitalize())
print('i am python'.title())
print(a.startswith("H"))
print(a.startswith("P"))
print(a.endswith("HON"))
print(a.endswith("N"))
'''
#
'''
b="hello java"
print(b.count('j'))
print(b.count('l'))
print(b.find('v'))
print(b.index('h'))
print(b.rindex('a'))
print(b.rfind('l'))
print("SALEM".casefold())
'''
#
'''
a="hello PYTHON"
print(a.swapcase())
print("i am {} from {}".format("vimal","salem"))
a='praveen'
b='frontend developer'
print(f'i am {a},i am {b}')
print("vimal".center(30,'*'))
print("vimal".ljust(30,'*'))
print("vimal".rjust(30,'*'))
print("      vimal     ".strip())
print("      vimal     ".rstrip())
print("      vimal     ".lstrip())
'''
#
'''
s="java"
print(s)
print(s.replace("v","u"))
'''
#
'''
ss="7234"
l=ss.split(" ")
print(l)
print(" ".join(l))
print("".join(l))
'''
#checking
'''
print("hello".isalpha())
print("hello2".isalpha())
print("123".isnumeric())
print("123e".isnumeric())
print("123abc".isalnum())
print("123#abc".isalnum())
print("name_1".isidentifier())
print("HELLO JAVA".isupper())
print("vimal".isupper())
print("HELLO JAVA".islower())
print("hello java".islower())
print("Hello Java".istitle())
print("hELLO jAVA".isupper())
'''

#encode and decode
'''
x="hi python"
print(x)
e=x.encode("UTF-32")
print("e:",e)
d=e.decode("UTF-32")
print("d:",d)
'''
#
'''
print("hi\npraveen")
print("hi\npraveen\tkumar")
print("hi\tpraveen\tkumar".expandtabs(8))
print("hi\npraveen\nkumar".splitlines())
'''
#reverse a string
#program

y=input("enter the n:")
l=" "
for i in y:
    l=i+l
print(l)    

