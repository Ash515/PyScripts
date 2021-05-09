from typing import NewType


class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList():
    def __init__(self):
        self.head=None
    def add_beginning(self,data):
       
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        n=self.head
        new_node=Node(data)
        if n is None:
            new_node=n
        else:
            while n.ref is not None:
                n=n.ref
              
            n.ref=new_node
    def add_after(self,data,x):
         
         n=self.head
         while n is not None:
             if(x==n.data):
                 break
             n=n.ref
         if n is None:
             print("No any x found")
         else:
             new_node=Node(data)
             
             new_node.ref=n.ref
             n.ref=new_node
    def add_before(self,data,y):
        n=self.head
        
        while n is not None:
            if(y==n.data):
                break
            n=n.ref
        if n is None:
            print("No y objecty found")
        else:
            



            



        




        
    def traverse(self):
        n=self.head
        if n is None:
            print("Empty list")
        while n is not None:
            print(n.data,"---->",end="")
            n=n.ref
    



ll=LinkedList()
ll.add_beginning(10)
ll.add_beginning(20)
ll.add_beginning(30)
ll.add_end(50)
ll.add_after(60,20)

ll.traverse()


        