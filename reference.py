#iterator
# l=[1,2,3,4,5,6,7]
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(i.__next__())
# print(i.__next__())

#generator
# def demo():
#     a=10
#     b=20
#     yield a
#     yield b
#     yield 33
# y=demo()
# print(next(y))
# print(next(y))
# print(next(y))

#closure
# def outer():
#     print("hello gowtham")
#     def inner():
#         print("hello vimal")
#     inner()
# outer()

#decorator
# def greeting(g):
#     g1=g
#     def inner():
#         print("hi")
#         g1()
#     inner()
#     print("hello gowtham")
# @greeting
# def name():
#     print("virat")
#
