#controle statemant
#1.sequential control
# print('START')
# X=10
# Y=20
# Z=X+Y
# print('SUM:',Z)
# print('END')
# --------------------------------------------------------------------------------------
#conditional control
#1.if statement
# a = int(input("enter the number:"))
# if a==10:
#     print("yes")

#2.if else statement
# a=int(input("enter the number:"))
# if a==10:
#     print("yes")
# else:
#     print("no")

#positive and negitive
# v = float(input("Enter value :"))
# if v>0:
#     print(v,"is positive number")
# else:
#     print(v,"is negative number")

#give word are vowel or not
# v=str(input("enter a to z:"))
# if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
#     print(v,"is a vowels sound")
# else:
#     print(v,"is consont sound")

# a = int(input("enter your age:"))
# if a >= 18:
# 	print('You Are Eligible to Vote')
# else:
# 	print('You Are Not Eligible to Vote')

#elif statement
# c = input("enter the word:")
# if c == "green":
#     print("g")
# elif c == "red":
#     print("r")
# elif c == "yellow":
#     print("y")
# else:
#     print("no")
#
# i = int(input("enter the number:"))
#
# if i == 10:
#     print("i is 10")
#
# elif i == 15:
#     print("i is 15")
#
# elif i == 20:
#     print("i is 20")
#
# else:
#     print("i is not present")

# score = 75
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
# 	print("Grade: F")

#nested if statement

# a = input("enter the email:")
# if a == "vimal@gmail.com":
#     print("correct")
#     b = input("enter the pass:")
#     if b == "1234":
#         print("correct pass")
#     else:
#         print("wrong pass")
# else:
#     print("wrong email")

# a=input("enter the email:")
# b=input("enter the password:")
# if a == "vimal@gmail.com":
#     if b == "1234":
#         print("login successfully")
#     else:
#         print("give pass is wrong")
# else:
#     print("wrong email")

# age = int(input("enter your age:"))
#
# has_license = True
#
# if age >= 18:
#     print("You are old enough to drive.")
#
#     if has_license:
#         print("You have a license and can legally drive.")
#
#     else:
#         print("You need to get a driver's license to legally drive.")
# else:
#     print("You are not old enough to drive.")

#for loop
# for i in range(1,6,2):
#     print(i)

# for e in range(5,0,-1):
#          print(e)

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(j,end=" ")
#     print()

#full pramid
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(j,end=" ")
#     for j in range(i):
#         print(j,end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(2*(n-i)-1):
#         if j == 0 or j == 2*(n-i)-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# count = 0
# while count < 5:
# 	print(count,end=" ")
# 	count +=1

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     print(i)
#
#
# a=[10,25,3,78,50]
# second = a[0]
# # largest = a[0]
# for i in a:
#     if i>second and i!=largest:
#         second=i
#     print(second)
#
# n=2
# for i in range(2,n):
#     if n%i == 0:
#         print("notp")
#         break
# else:
#     print("yes")

# a = int(input("enter the num:"))
# for i in range(1,a+1):
#     if i%3==0 and i%5==0:
#         print("fizz_buzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# num1 = [4,3,9]
# num2 = [1,2,4,5,6,9,9,4]
# num3 = [ ]
# for i in num2:
#     if i in num1 and i not in num3:
#         num3.append(i)
# print(num3)











