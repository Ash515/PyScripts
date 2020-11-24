import tkinter as tk
from tkinter import *
import socket
import sys
import time

root=Tk()
root.geometry("500x500")
root.title("Ash-Chat")
def Host():
    s=socket.socket()
    host=socket.gethostname()
    print("Server will start on host:",host)
    port=5005
    s.bind((host,port))
    print("Server is bind successfully")
    s.listen(5)
    conn,addr=s.accept()
    print(addr,"has connected")
while 1:
    msg=input(str("You:>>"))
    msg=msg.encode()
    conn.send(msg)
    incoming_msg=conn.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Client:>>",incoming_msg)

def server():
    s=socket.socket()
    host=input(str("Please enter host name:"))
    port=5005
try:
    s.connect((host,port))
    print("Connected to server")
except:
    print("Connection to server is failed:(")
while 1:
    incoming_msg=s.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Server:>>",incoming_msg)
    msg=input(str("You:>>"))
    msg=msg.encode()
    s.send(msg)
    
   
       



root.config(bg="pink")

l=Label(root,text="Chat with Me..",font=('verdana',15,'bold'),bg="black",fg="white")
l.place(x=180,y=10)
text=ScrolledText(root,width=40,height=10)
text['font']=('verdana',10,'bold')
text.place(x=50, y=30)















root.mainloop()
