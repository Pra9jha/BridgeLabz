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

s=Stack()
s1=Stack()
for i in range(2,1000+1):
    if primeOrNot(i):
        s.push(str(i))


for i in range(s.size()-1):
    for j in range(s.size()):
         if anagram(s.elementAt(i),s.elementAt(j)) and i!=j :
            s1.push(s.elementAt(i))
            break

for i in range(s1.size()):
    print(s1.poop(),end=" ")
