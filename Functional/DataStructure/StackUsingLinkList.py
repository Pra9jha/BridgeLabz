class Node:
    data=0
    next=None
class Stack:
    head=None
    top=-1
    def push(self,value):
        n=Node()
        n.data=value
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=n
        self.top=self.top+1
    def poop(self):
        self.top=self.top-1
        return self.elementAt((self.top)+1)

    def size(self):
        if self.top<=-1:
            return 0
        else:
            return self.top+1

    def elementAt(self,index):
        temp=self.head
        for i in range(0,index):
            temp=temp.next
        return temp.data

    def show(self):
        temp=self.head
        for i in range(self.size()):
            print(temp.data,end=" ")
            temp=temp.next


    def peep(self):
        temp = self.head
        for i in range(self.size()-1):
            temp = temp.next
        return temp.data
