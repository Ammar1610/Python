class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Stack:
    def __init__(self):
        self.head=None
    def print_stack(self):
        n=self.head
        if n is None:
            self.head=n
        else:
            while n is not None:
                print(n.data)
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:    
            self.head=self.head.ref

LL=Stack()
LL.push(10)
LL.push(20)
LL.push(40)
LL.pop()
LL.print_stack()

