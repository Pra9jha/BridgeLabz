import random
class Node:
    data=0
    next=None
class Queue:
    head=None
    rear=-1
    front=-1
    def enqueue(self,value):
        n=Node()
        n.data=value
        if self.rear==-1 and self.front==-1:
            self.head=n
            self.front=self.front+1
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next = n
        self.rear=self.rear+1
    def dequeue(self):
       if self.size()==-1:
           print("Underflow")
       else:
        self.front=self.front+1
        temp=self.head
        self.head = self.head.next
        return temp.data
    def elementAt(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp.data
    def show(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
            print("________________________________________")
    def size(self):
        if self.front and self.rear==-1:
            return -1
        else:
            return (self.rear-self.front)+1
# q=Queue()
# for i in range(10):
#     q.enqueue(i)
#
# while q.size()>0:
#     print("into q.size")
#     print(q.dequeue())
#
#
