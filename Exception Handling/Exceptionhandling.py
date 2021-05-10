def grade(m1,m2,m3):
    try:
        grade=(m1+m2+m3)/0
        if(grade<90):
            print("O")
        elif(grade>70 and grade<90):
            print("A")
        elif(grade>50 and grade <69):
            print("B")
        else:
            print("C")
    except NameError:
        print("Somethong is not good")
    except:
        print("Sorry...please check your calculation")
maths=int(input("Maths mark:"))
physics=int(input("Physics mark:"))
chemistry=int(input("chemistry mark:"))
grade(maths,physics,chemistry)








