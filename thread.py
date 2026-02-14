#single thread
import threading as t
# def book(n):
#     print("book name:",n)
# t1=t.Thread(target=book,args=("python",))
# t1.start()

#multi level thread
# def ktm(n):
#     print("bike name:",n)
# def owner(a):
#     print("owner name:",a)
# t1=t.Thread(target=ktm,args=("duke200",))
# t2=t.Thread(target=owner,args=("vimal",))
# t1.start()
# t2.start()

#dameon thread
def book(n):
    print("book name:",n)
t1=t.Thread(target=book,args=("java",))
t1.setDaemon(False)
print(t1.isDaemon())
t1.start()