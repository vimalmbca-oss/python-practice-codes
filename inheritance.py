#single inheritance

class father:
    def fun1(self):
        print("father money")
class son(father):
    def fun2(self):
        print("money need")
d=son()
d.fun2()
d.fun1()

# #multilevel inheritance
#
# class gf:
#     def fun1(self):
#         print("thatah money")
# class father(gf):
#     def fun2(self):
#         print("father money")
# class son(father):
#     def fun3(self):
#         print("money need")
# d=son()
# d.fun3()
# d.fun2()
# d.fun1()
#
# #hierachical inheritance
#
# class father:
#     def fun1(self):
#         print("father money")
# class son1(father):
#     def fun2(self):
#         print("money need")
# class son2(father):
#     def fun3(self):
#         print("money need")
# s=son1()
# s.fun2()
# s.fun1()
# s1=son2()
# s1.fun3()
# s1.fun1()
#
# #multiple inheritance
#
# class gf:
#     def fun1(self):
#         print("thatha money")
# class father:
#     def fun2(self):
#         print("father money")
# class son(father,gf):
#     def fun3(self):
#         print("money need")
# s1=son()
# s1.fun1()
# s1.fun2()
# s1.fun1()
#
# #hybrid inheritance
#
# class father:
#     def fun1(self):
#         print("father money")
# class son1(father):
#     def fun2(self):
#         print("money for brother")
# class son2(father):
#     def fun3(self):
#         print("money for brother")
# class son3(son1,son2):
#     def fun4(self):
#         print("money need")
# s1=son3()
# s1.fun4()
# s1.fun3()
# s1.fun2()
# s1.fun1()
#




















