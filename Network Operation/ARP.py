print("To find the arp protocols")
IP=["192.108.0.64","192.168.0.60","192.168.0.68","132.147.3.3"]
Ethernet=["0_10_A_u","1_20_L_4","56_3_P_k","O_84_3_9"]
print("Choose your Option: 1.ARP 2.EXIT")
choice=int(input("Enter your choice:"))
if (choice==1):
   ipaddr=str(input("Enter your IP adress:"))
   for i in IP:
    if(ipaddr==i):
        print("Your IP address match")
        if(ipaddr=="192.108.0.64"):
            print("Your Ethernet address is",Ethernet[0])
        elif(ipaddr=="192.168.0.60"):
            print("Your Ethernet address is",Ethernet[1])
        elif(ipaddr=="192.168.0.68"):
            print("Your Ethernet address is",Ethernet[2])
        elif(ipaddr=="132.147.3.3"):
            print("Your Ethernet address is",Ethernet[3])
else:
    print("Bye!!!")
    exit(1)
