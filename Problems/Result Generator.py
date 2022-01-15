print("Ashwin School of Technology (Autonomous)")
print("Department of Examination")
print("CGPA Calculator")
name=input("Enter Name :")
reglist=[]
num=212218205000
while num<=212218205011:
    reglist.append(num)
    print(reglist)
    num=num+1
   
if(8 in reglist):
    print("value in")
else:
    print("not in") 
       #regno=int(input("enter reg no:"))
   # if(regno not in reglist):
       # print("wrong value")
       # continue
    #else:**/
        

regulation=int(input("Choose your Regulation here: 1.2017\n 2.2019\n"))
if(regulation==1):
    Dept=int(input("Select your department:1.IT\n 2.EEE\n 3.CSE\n 4.ECE\n 5.MECH\n 6.EIE\n"))
    if(Dept==1):
        sem=int(input("Semester :1\n2\n3\n4\n5\n6\n7\n8"))
        if(sem==1):
            print("Subjects\n")
            print("1.English\n2.Mathematics\n3.Physics\n4.Chemistry\n5.Python")
            eng=int(input("Enter your English Marks: "))
            maths=int(input("Enter your Mathematics Marks: "))
            phy=int(input("Enter your Physics Marks: "))
            chem=int(input("Enter your Chemistry Marks: "))
            python=int(input("Enter your Python Marks: "))
            total=eng+maths+phy+chem+python
            avg=total/5
            if(90<avg<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg)
            elif(70<avg<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg)
            elif(50<avg<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg)
            elif(35<avg<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg)
        elif(sem==2):
            print("Subjects\n")
            print("1.English\n2.Mathematics\n3.Physics\n4.ITE\n5.C programming")
            eng2=int(input("Enter your English Marks: "))
            maths2=int(input("Enter your Mathematics Marks: "))
            phy2=int(input("Enter your Physics Marks: "))
            ite=int(input("Enter your ITE Marks: "))
            cpro=int(input("Enter your C programming Marks: "))
            total2=eng2+maths2+phy2+ite+cpro
            avg2=total2/5
            if(90<avg2<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg2)
            elif(70<avg2<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg2)
            elif(50<avg2<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg2)
            elif(35<avg2<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg2)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg2)
        elif(sem==3):
            print("Subjects\n")
            print("1.DS\n2.Mathematics\n3.JAVA\n4.DPSD\n5.ADC")
            ds=int(input("Enter your DS Marks: "))
            maths3=int(input("Enter your Mathematics Marks: "))
            java=int(input("Enter your JAVA Marks: "))
            dpsd=int(input("Enter your DPSD Marks: "))
            adc=int(input("Enter your ADC Marks: "))
            total3=ds+maths3+java+dpsd+adc
            avg3=total3/5
            if(90<avg3<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg3)
            elif(70<avg3<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg3)
            elif(50<avg3<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg3)
            elif(35<avg3<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg3)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg3)
        else:
            print("Subjects\n")
            print("1.DAA\n2.Mathematics\n3.DBMS\n4.OS\n5.CA")
            daa=int(input("Enter your DAA Marks: "))
            maths4=int(input("Enter your Mathematics Marks: "))
            dbms=int(input("Enter your DBMS Marks: "))
            os=int(input("Enter your OS Marks: "))
            ca=int(input("Enter your CA Marks: "))
            total4=daa+maths4+dbms+os+ca
            avg4=total4/5
            if(90<avg4<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg4)
            elif(70<avg4<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg4)
            elif(50<avg4<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg4)
            elif(35<avg4<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg4)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg4)
    elif(Dept==2):
        sem2=int(input("Semester :1\n2\n3\n4\n5\n6\n7\n8"))
        if(sem2==1):
            print("Subjects\n")
            print("1.English\n2.Mathematics\n3.Physics\n4.Chemistry\n5.Python")
            eng5=int(input("Enter your English Marks: "))
            maths5=int(input("Enter your Mathematics Marks: "))
            phy5=int(input("Enter your Physics Marks: "))
            chem5=int(input("Enter your Chemistry Marks: "))
            python5=int(input("Enter your Python Marks: "))
            total5=eng5+maths5+phy5+chem5+python5
            avg5=total5/5
            if(90<avg5<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg5)
            elif(70<avg5<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg5)
            elif(50<avg5<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg5)
            elif(35<avg5<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg5)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg5)
        elif(sem2==2):
            print("Subjects\n")
            print("1.English\n2.Mathematics\n3.Physics\n4.BEEE\n5.C programming")
            eng6=int(input("Enter your English Marks: "))
            maths6=int(input("Enter your Mathematics Marks: "))
            phy6=int(input("Enter your Physics Marks: "))
            beee=int(input("Enter your BEEE Marks: "))
            cpro2=int(input("Enter your C programming Marks: "))
            total6=eng6+maths6+phy6+beee+cpro2
            avg6=total6/5
            if(90<avg6<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg6)
            elif(70<avg6<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg6)
            elif(50<avg6<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg6)
            elif(35<avg6<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg6)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg6)
        elif(sem2==3):
            print("Subjects\n")
            print("1.EC\n2.Mathematics\n3.JAVA\n4.DPSD\n5.MPMC")
            ec=int(input("Enter your EC Marks: "))
            maths7=int(input("Enter your Mathematics Marks: "))
            java2=int(input("Enter your JAVA Marks: "))
            dpsd2=int(input("Enter your DPSD Marks: "))
            mpmc=int(input("Enter your MPMC Marks: "))
            total7=ec+maths7+java+dpsd+mpmc
            avg7=total7/5
            if(90<avg7<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg7)
            elif(70<avg7<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg7)
            elif(50<avg7<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg7)
            elif(35<avg7<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg7)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg7)
        else:
            print("Subjects\n")
            print("1.Network\n2.Mathematics\n3.DBMS\n4.OS\n5.CA")
            ntw=int(input("Enter your Network Marks: "))
            maths8=int(input("Enter your Mathematics Marks: "))
            dbms2=int(input("Enter your DBMS Marks: "))
            os2=int(input("Enter your OS Marks: "))
            ca2=int(input("Enter your CA Marks: "))
            total8=ntw+maths8+dbms2+os2+ca2
            avg8=total8/5
            if(90<avg8<=100):
                print("Congratulations !!!\n Teriffic performance\n CGPA is",avg8)
            elif(70<avg8<=89):
                print("Congratulations !!!\nAmazing performance\n CGPA is",avg8)
            elif(50<avg8<=69):
                print("Congratulations !!!\n Very good performance\n CGPA is",avg8)
            elif(35<avg8<=49):
                print("Congratulations !!!\nGood performance\n CGPA is",avg8)
            else:
                print("Sorry !!!\n Poor performance \n CGPA is",avg8)
else:
    print("work under construction")            





