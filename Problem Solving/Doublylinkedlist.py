class Node:
    def __init__(self,data):
        self.data=data
       
        self.head=None
        
class Doublelist:
    def __init__(self,pref,nref):
       self.head=None
       self.pref=pref
       self.nref=nref
    
    def traverse(self):
        n=self.head
        if n is None:
            print("There is no any node")
        else:
            while n is not None:
                print(n)
            n=n.nref
    def add_begin(self,data):
        n=self.head
        new_node=Node()
        if n is None:
            n=new_node
        else:
            n.pref=new_node.nref
            n=new_node







dl=Doublelist()
dl.traverse()
dl.add_begin(10)

        

