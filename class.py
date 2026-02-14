#class and object

class car:
    brand=None
    colour=None
    model=None
    price=None
    def engine(self):
        print(self.brand,"car start run off")
    def gear(self):
        print(self.model,"gear helps to change gears")
car1=car()
car1.brand="tata"
car1.price="150000"
car1.colour="red"
car1.model="nexon"
print("brand:",car1.brand)
print("model:",car1.model)
print("price:",car1.price)
print("colour:",car1.colour)
car1.engine()
car1.gear()
print("---------------------")
car2=car()
car2.brand="bmw"
car2.price="1500000"
car2.colour="red"
car2.model="m3"
print("brand:",car2.brand)
print("model:",car2.model)
print("price:",car2.price)
print("colour:",car2.colour)
car2.engine()
car2.gear()            

'''
#constructor
class mobile:
    brand=None
    colour=None
    model=None
    price=None
    def button(self):
        print(self.brand,"button used to run off")
        print("end".center(25,"*"))
    def __init__(self,b,m,c,p):
        self.brand=b
        self.price=p
        self.colour=c
        self.model=m
        print("brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)
        print("colour:",self.colour)
        self.button()        
m=mobile("vivo","15000","white","v20 bro")    
m1=mobile("realme","15000","white","z1pro")    
'''    

































