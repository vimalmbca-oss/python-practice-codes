#class and abjects
#1.laptop
'''
class lap:
    brand=None
    RAM=None
    price=None
    def details(self):
        print(self.brand,"fastest running laptop")
    def processor(self):
        print(self.RAM,"with have itel intercore processor")
lap1=lap()
lap1.brand="lenovo"
lap1.RAM="4gb RAM"
lap1.price="35000"
print("brand:",lap1.brand)
print("RAM:",lap1.RAM)
print("price:",lap1.price)
lap1.details()
lap1.processor()
print("----------------------")
lap2=lap()
lap2.brand="sony 5pro"
lap2.RAM="12gb RAM"
lap2.price="65000"
print("brand:",lap2.brand)
print("RAM:",lap2.RAM)
print("price:",lap2.price)
lap2.details()
lap2.processor()
'''
#2.student details

class stud:
   student=None
   tamil=None
   eng=None
   maths=None
   sci=None
   soc=None
   def school(self):
       print("----gov.her.sec.school----")
   def grade(self):
       print("----student marksheet----")
   def subjest(self):
       print("-------subjects-------")
stud1=stud()
stud1.school()
stud1.grade()
stud1.student="vimal"
stud1.tamil="A grade"
stud1.eng="B+ grade"
stud1.maths="D grade"
stud1.sci="C+ grade"
stud1.soc="A+ grade"
print("student:",stud1.student)
stud1.subjest()
print("tamil:",stud1.tamil)
print("eng:",stud1.eng)
print("maths:",stud1.maths)
print("sci:",stud1.sci)
print("soc:",stud1.soc)
print("-----------------")
stud2=stud()
stud2.school()
stud2.grade()
stud2.student="logesh"
stud2.tamil="C+ grade"
stud2.eng="B grade"
stud2.maths="A= grade"
stud2.sci="D+ grade"
stud2.soc="C grade"
print("student:",stud2.student)
stud2.subjest()
print("tamil:",stud2.tamil)
print("eng:",stud2.eng)
print("maths:",stud2.maths)
print("sci:",stud2.sci)
print("soc:",stud2.soc)

#3.calculator
'''
class calc:
    add=None
    sub=None
    mult=None
    div=None
    def cal(self):
        print("----calculate two numbers----")
calc1=calc()
calc1.cal()
a=int(input("enter the number:"))
b=int(input("enter the number:"))
calc1.add=a+b
calc1.sub=a-b
calc1.mult=a*b
calc1.div=a/b
print("add:",calc1.add)
print("sub:",calc1.sub)
print("mult:",calc1.mult)
print("div:",calc1.div)
print("-------------")
calc2=calc()
calc2.cal()
a=int(input("enter the number:"))
b=int(input("enter the number:"))
calc2.add=a+b
calc2.sub=a-b
calc2.mult=a*b
calc2.div=a/b
print("add:",calc2.add)
print("sub:",calc2.sub)
print("mult:",calc2.mult)
print("div:",calc2.div)
'''
#constructor
'''
#1.employee
class employee:
    name=None
    ID=None
    salary = None
    def company(self):
        print("---TCS company---")
    def __init__(self,n,i,s):
        self.company()
        self.name=n
        self.ID=i
        self.salary=s
        print("name:",self.name)
        print("ID:",self.ID)
        print("salary:",self.salary)
emp1=employee("vimal","23145","35000")
emp2=employee("logesh","43567","45000")
'''































