from abc import ABC,abstractmethod
class ebook(ABC):
    @abstractmethod
    def data(self):
        print("book name:learn python")
        print("book author:vimal")
        print("main data")
    @abstractmethod
    def data1(self):
        print("book name:learn java")
        print("book author:logesh")
        print("main data")
    def data2(self):
        print("book name:learn c++")
        print("book author:rahul")
class vendor(ebook):
    def data(self):
        print("book name:learn python")
        print("book author:vimal")
    def data1(self):
        print("book name:learn java")
        print("book author:logesh")
v=vendor()
v.data()
v.data1()
v.data2()




