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
    def size(self):
        if self.front and self.rear==-1:
            return -1
        else:
            return (self.rear-self.front)+1

def primeOrNot(num):
    for i in reversed((range(2 , int(num/2)+1))):
        if num%i==0:
            return False
    return True
def anagram(val1,val2):
    val1=sorted(val1)
    val2=sorted(val2)
    if val1==val2:
      return True
    else:
       return False

q=Queue()
q1=Queue()
for i in range(2,1000+1):
    if primeOrNot(i):
        q.enqueue(str(i))

for i in range(q.size()-1):
    for j in range(q.size()):
         if anagram(q.elementAt(i),q.elementAt(j)) and i!=j :
            q1.enqueue(q.elementAt(i))
            break
for i in range(q1.size()):
    print(q1.dequeue(),end=" ")