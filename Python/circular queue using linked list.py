class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        if self.front is None:
            self.front = node(data)
            self.rear = self.front
            self.rear.next = self.front
        else:
            newnode = node(data)
            self.rear.next = newnode
            self.rear = newnode
            self.rear.next = self.front
    def dequeue(self):
        self.front = self.front.next
        self.rear.next = self.front
    def display(self):
        temp = self.front
        while temp.next is not self.front:
            print(id(temp),temp.data,id(temp.next))
            temp = temp.next
        print(id(temp),temp.data,id(temp.next))    
obj = queue()
n = int(input())
for i in range(n):
    ele = int(input())
    obj.enqueue(ele)
obj.display()
obj.dequeue()
obj.display()

            
        
