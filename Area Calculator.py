import math
print("Area Calculator")
def Circle(radius):
    cir_res=pi*radius*2
    return cir_res
def Square(a):
    sq_res= 2*a
    return sq_res
def Triangle(length,breadth,height):
    s=float(length+breadth+height)/2
    tri_res=math.sqrt(s*(s-length)*(s-breadth)*(s-height))
    return tri_res
def Rectangle(length,breadth):
    rect_res=length*breadth
    return rect_res
print("1.Circle 2.Square 3.Rectangle 4.Triangle  5.Exit")
choice=int(input("Enter your choice:"))
if(choice==1):
    r=int(input("Enter Radius value:"))
    print("Area of Circle is,",Circle(r))
elif(choice==2):
    sq=int(input("Enter radius value:"))
    print("Area of Square is,",Square(sq))

elif(choice==3):
    rec_len=int(input("Enter length:"))
    rec_breadth=int(input("Enter Breadth:"))
    print("Area of Reactangle is,",Rectangle(rec_len,rec_breadth))
elif(choice==4):
    tri_len=int(input("Enter length:"))
    tri_breadth=int(input("Enter Breadth:"))
    tri_height=int(input("Enter Height :"))
    print("Area of Triangle is,",Triangle(tri_len,tri_breadth,tri_height))
else:
    exit(0)
