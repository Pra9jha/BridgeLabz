class Node:
     def __init__(self,data):
         self.next=0
         self.data=data

class LinkList:
    head=0
    def  insert(self,value):
        n=Node(value)
        if self.head==0:
            self.head=n
        else:
            temp=self.head
            while(temp.next!=0):
                temp=temp.next
            temp.next=n

    def insertat(self,pos,value):
      if pos==0:
          self.insertatStart(value)
      else:
        n = Node(value)
        n.data=value
        temp=self.head
        for  i in range(1,pos):
            temp=temp.next
        tn=temp.next
        temp.next=n
        n.next=tn
    def insertatStart(self,value):
        n=Node(value)
        n.data=value
        temp=self.head
        n.next=temp
        self.head=n

    def insertOrdered(self,value):
        temp=self.head
        if self.size()==0:
            self.insert(value)
        else:
            if value<self.head.data:
                self.insertatStart(value)
            else:
               try:
                  while temp.data<value:
                        temp=temp.next
                  self.insertat(self.indexof(temp.data), value)
               except :
                   self.insert(value)

    def indexof(self,value):
        temp=self.head
        i=0

        while temp!=0 and value!=temp.data :
            i=i+1
            temp=temp.next
        if  value==temp.data:
            return i

    def size(self):
        temp=self.head
        s=0
        while temp!=0:
            s=s+1
            temp=temp.next
        return s

    def delete(self,value):
      if value==self.head.data:
          self.head=self.head.next
      else:
        temp=self.head
        while temp.next.data!=value:
            temp=temp.next
        tn=temp.next.next
        temp.next=tn

    def search(self,value,fn):
        temp = self.head
        flag=0
        while temp!=0:
          if temp.data==value:
              self.delete(value)
              self.saveTofile(fn)
              flag=1
              break
          temp = temp.next
        if flag==0 :
         print("Element not found")
         self.insertOrdered(value)
         self.saveTofile(fn)

    def saveTofile(self,fn):
        str=""
        temp=self.head
        while temp!=0:
            str=str+" "+temp.data
            temp=temp.next
        open(fn,'w').write(str)

    def show(self):
        temp = self.head
        while(temp!=0):
            print(temp.data,end=" ")
            temp=temp.next
        print()

ll=LinkList()
fn , word = input("Enter the file name use comma and Enter the word to search\n      eg t.txt,my::\n ").split(",")
o= open(fn, 'r')
f =o.read()
store = ""
for i in range(len(f)):
    if (f[i] != " "):
        store = store + f[i]
    if f[i] == " " or i == len(f) - 1:
        ll.insertOrdered(store)
        store = ""
ll.show()
ll.search(word,fn)
o.close()
# to display the content in the file after making change
print(open(fn).read())






