from PIL import Image
print("------colour option------")
print("1.view colours\n2.skip")
ch=int(input("enter your choice:"))
if ch==1:
    print("1.orange\n2.black\n3.silver")
    ch=int(input("enter colour:"))
    if ch==1:
        print("orange")
        img=Image.open(r"C:\Users\Alex\Downloads\download (2).jfif")
        img.show()
    elif ch==2:
        print("black")
        img=Image.open(r"C:\Users\Alex\Downloads\download (2).jfif")
        img.show()
    elif ch==3:
        print("silver")
        img=Image.open(r"C:\Users\Alex\Downloads\download (2).jfif")
        img.show()
        print("----------------------")
elif ch==2:
    print("----------------------")
    print("offers")

        
        
    
