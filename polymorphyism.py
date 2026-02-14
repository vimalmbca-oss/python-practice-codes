#method overloading
"""
class cal:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("4 args add value:",a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print("3 args add value:",a+b+c)
        elif a!=None and b!=None:
            print("2 args add value:",a+b)
        elif a!=None:
            print("1 args add value:",a)
c=cal()
c.add(40,30,20,10)
c.add(40,30,20)
c.add(40,30)
c.add(40)
"""
#method overriding
"""
class a:
    def fun1(self):
        print("hello java")
class b(a):
    def fun1(self):
        super().fun1()
        print("hello python")
B=b()
B.fun1()
"""
        
            
