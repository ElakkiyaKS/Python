class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        if self.head is None:
            self.head = node(data)
        else:
            newnode = node(data)
            newnode.next = self.head
            self.head = newnode
    def pop(self):
        self.head = self.head.next
    def peek(self):
        temp = self.head
        print(temp.data)
    def display(self):
        temp = self.head
        while temp is not None:
            print(id(temp),temp.data,id(temp.next))
            temp = temp.next
obj = stack()
n = int(input())
for i in range(n):
    ele = int(input())
    obj.push(ele)
obj.display()
obj.pop()
obj.display()
obj.peek()
