#core data types
#tuple
'''
a=(1,2,3,4,5,"ram",(10,11,12))
print(type(a))
print(a)
print(len(a))
b=(3,12,19,23)
print(min(b))
print(max(b))
print(a[5][2])
print(a[2:4])
print(a[-1])
print(a[2:6:2])
print(a+b)
print(a*3)
'''
#list
'''
a=[1,2,3,"ravi"]
print(type(a))
print(a)
print(len(a))
b=[3,12,19,23]
print(min(b))
print(max(b))
print(a[1])
print(a[3][1])
print(a[0:4])
print(a+b)
print(a*2)
'''

a=[1,2,3]
'''
a.append(10)
print(a)
a.extend((100,200,"ram"))
print(a)
a.insert(2,5)
print(a)
a.remove(100)
print(a)
a.pop(1)
print(a)
a.pop()
print(a)
'''
a.sort()
print(a)
'''
a.reverse()
print(a)
a.clear()
print(a)
c=[23,45,65]
b=c.copy()
print(b)
'''
#set
'''
a={1,2,3,1,2}
print(a)
print(type(a))
print(len(a))
print(min(a))
print(max(a))
a.add(5)
print(a)'
b={10,20}
a.update(b)
print(a)
a.remove(5)
print(a)
a.discard(1)
print(a)
a.pop()
print(a)
print(sorted(a))
a={1,2,3,4}
b={1,2,}
c =  a.issubset(b)
print(c)
d = a.issuperset(b)
print(d)
e = b.issubset(a)
print(e)
f=a.union(b)
print(f)
g=a.intersection(b)
print(g)
h=a.isdisjoint(b)
print(h)
a={1,2,3,4}
b={1,2,5}
i=a.difference(b)
print(i)
j=b.difference(a)
print(j)
k=a.symmetric_difference(b)
print(k)
'''
#distionary
'''
a={"name":("ram","raj"),"age":2}
print(a)
print(type(a))
print(a.keys())
print(a.values())
print(a.items())
print(a.get("age"))
a.update({"place":"salem"})
print(a)
a.pop("age")
print(a)
a.popitem()
print(a)
b={"a":[10,20,"ram","ravi"],"b":20}
c=b.get("a")
print(c)
c.append(100)
print(c)
b.setdefault("b",30)
print(b)
a=(1,2,3)
b=(10,20,30)
c=dict.fromkeys(a,b)
print(c)
'''








