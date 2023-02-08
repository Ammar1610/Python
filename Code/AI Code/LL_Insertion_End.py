class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None
    def  print_ll(self):           
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref           
    def insert_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=new_node   
            new_node.ref=None     
LL=Linked_List()
n=int(input("Enter number of nodes:"))
for i in range(0,n):
    a=eval(input("Enter data:"))
    LL.insert_end(a)
LL.print_ll()