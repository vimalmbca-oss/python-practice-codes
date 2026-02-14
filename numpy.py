# y = str(input("enter the string"))
# l = ""
# for i in y:
#     l=i+l
# if l == y:
#     print("yes")
# else:
#     print("no")

a = [1,2,3,3,4,5,5,7,8,9]
b = []

for i in a:
    if i not in b:
       b.append(i)
print(b)



# a,b = 0,1
# for i in range(10):
#     print(a, end="")
#     a,b=b,a+b
#
# a=int(input("enter the number:"))
# b=0
# c=1
# t=a
# while t>0:
#     d=t%10
#     b=b+d
#     c=c*d
#     t=t//10
#     d=b+c
# if a==d:
#     print(a,"is a special number")
# else:
#     print(a,"is not special number")

# import math
#
# a = int(input("Enter the number: "))
# t = a
# sum_fact = 0
#
# while t > 0:
#     d = t % 10
#     sum_fact = sum_fact + math.factorial(d)
#     t = t // 10
#
# if a == sum_fact:
#     print(a, "is a special number")
# else:
#     print(a, "is not a special number")


# a = int(input("Enter the number: "))
# t = a
# sum_fact = 0
#
# while t > 0:
#     d = t % 10
#
#     # factorial of digit (without math)
#     fact = 1
#     for i in range(1, d + 1):
#         fact = fact * i
#
#     sum_fact = sum_fact + fact
#     t = t // 10
#
# if a == sum_fact:
#     print(a, "is a special number")
# else:
#     print(a, "is not a special number")
# a=int(input("enter the number:"))
# b=0
# t=a
# while t>0:
#     d=t%2
#     b=b+d
#     t=t//2
# if b>0:
#     print(a,"is a harshad number")
# else:
#     print(a,"is not harshad number")

#find harshas number
# a = int(input("Enter the number: "))
# t = a
# digit_sum = 0
#
# while t > 0:
#     d = t % 10          # get last digit
#     digit_sum += d     # add digit to sum
#     t = t // 10        # remove last digit
#
# if digit_sum != 0 and a % digit_sum == 0:
#     print(a, "is a Harshad number")
# else:
#     print(a, "is not a Harshad number")

#4.concatenate the two string

a=str(input("enter the string:"))
b=str(input("enter the string:"))
print(f'{a}{b}')

#5.check digits in string

# a="123t5"
# print(a.isdigit())

# string=str(input("enter the string:"))
# count_vowels = 0
# count_char = 0
# for v in string:
#     if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
#         count_vowels = count_vowels+1
#     else:
#         count_char = count_char + 1
# print("no of vowels in a sentance is:",count_vowels)
# print("no of char in a sentance is:",count_char)

#five number
# m1=int(input("enter mark 1:"))
# m2=int(input("enter mark 2:"))
# m3=int(input("enter mark 3:"))
# m4=int(input("enter mark 4:"))
# m5=int(input("enter mark 5:"))
# total=m1+m2+m3+m4+m5
#
#
# avg=total/5
# print("avg :",avg)
# if avg>=90 and avg<=100:
#     print("A+")
# elif avg>=80 and avg<90:
#     print("B+")
# elif avg>=70 and avg<80:
#     print("C+")
# elif avg>=60 and avg<70:
#     print("D+")
# elif avg>=50 and avg<60:
#     print("e+")
# else:
#     print("fail")


# m=str(input("enter the month:"))
# if m=='jan' or m=='mar' or m=='may' or m=='july' or m=='aug' or m=='oct' or m=='dce':
#     print("31 days")
# elif m=='april' or m=='jun' or m=='sept' or m=='nove':
#     print("30 days")
# elif m=='feb':
#     print("28 to 29 days")


#write a python program to display "hello" if the user enter the number that multipla
#by 5 athorwise print "bey".
# n=int(input("enter the number:"))
# if n%5==0:
#     print("hello")
# else:
#     print("bey")

# n1=int(input("enter nunber 1:"))
# n2=int(input("enter number 2:"))
# n3=int(input("enter number 3:"))
# if n1<=n2 and n1<=n3:
#     print(n1,"is mini number")
# elif n2<=n3 and n2<=n1:
#     print(n2,"is mini number")
# elif n3<=n2 and n3<=n1:
#     print(n3," is mini number")


# n1=int(input("enter nunber 1:"))
# n2=int(input("enter number 2:"))
# n3=int(input("enter number 3:"))
# if n1>=n2 and n1>=n2:
#     print(n1," is max number")
# elif n2>=n3 and n2>=n1:
#     print(n2," is max number")
# elif n3>=n2 and n3>=n1:
#     print(n3," is max number")

# a = int(input("enter:"))
# if a%2==0:
#     print("add")
# else:
#     print("even")
a= 10
odd=0
even=0
for i in range(1,a+1):
    if(i%2!=0):
        odd=odd+i
    else:
        even= even+i
print(odd)
print(even)
















#for i in range(127):
 #   print(chr(i),i)
#for i in range(96,64,-1):
 #   print(chr(i),i)
# fact=1
# for i in range(1,7):
#      fact=fact*i
# print(fact)
# a="mom"
# reverse=""
# for i in a:
#     reverse=i+reverse
# if a == reverse:
#     print("yes")
# else:
#     print("no")
# print(reverse,end="")
# a="mom"
# reverse="  "
# for i in a:
#    reverse=i+reverse
# if i==reverse:
#     print("palindrome")mmmm
# else:
#     print("not palindrome")




































