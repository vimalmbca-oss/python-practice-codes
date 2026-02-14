#create file
#c=open(r"C:\Users\Alex\Desktop\vimal.txt","x")
#c.close()
#print("file created")

#read file
#rd=open(r"C:\Users\Alex\Desktop\vimal.txt","r")
#content=rd.read()
#print(content)
#rd.close()

#write a file
"""
wd=open(r"C:\Users\Alex\Desktop\vimal.txt","w")
wd.write("hellow\nbey")
wd.close()
"""
#append file

wd=open(r"C:\Users\Alex\Desktop\vimal.txt","a")
wd.write("i am vimal")
wd.close()
rd=open(r"C:\Users\Alex\Desktop\vimal.txt","r")
content=rd.read()
print(content)
rd.close()

#delete the file
#import os
#os.remove(r"C:\Users\Alex\Desktop\vimal.txt")
