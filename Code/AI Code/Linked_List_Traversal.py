class Node:
    def __init__(self,data):
        self.data=None
        self.ref=None
class linked_list:
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

L1=Node(10)                    
L1=linked_list()
L1.print_ll()                    