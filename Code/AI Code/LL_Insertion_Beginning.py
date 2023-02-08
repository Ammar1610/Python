class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None
    def print_LL(self):
        n=self.head
        if n is None:
            print("Linked List is empty")
        else:
            while n is not None:
                print(n.data)
                n=n.ref
    def insert_beggining(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
LL=Linked_List()
LL.insert_beggining(10)
LL.insert_beggining(20)                
LL.print_LL()