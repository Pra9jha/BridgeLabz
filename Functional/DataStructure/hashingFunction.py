class Node:
    data=None
    next=None
class LinkList:
    head=None
    for i in range(11):
        n=Node()
        if head ==None:
            head=n
        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=n
    def insertat(self,value):
        nv = Node()
        temp=self.head
        nv.data = value
        pos=value%11
        # print("position is "+str(pos))
        for i in range(pos):
            temp=temp.next
        if temp.data==None:
            temp.data=nv
        else:
            temp=temp.data
            while temp.next!=None:
                temp=temp.next
            temp.next=nv

    def find(self,value,fn):
        flag=0
        prev=None
        pos=value%11
        temp=self.head
        for i in range(pos):
            temp=temp.next
        hdata=temp
        temp = temp.data
        while temp!=None :
            # print(temp.data)
            if value==temp.data:
                print("value found")
                self.deletefromfile(prev,temp,hdata)
                flag=1
            prev=temp
            temp=temp.next
            self.saveTofile(value, fn)
        if temp==None and flag==0:
            print("value is not found")
            self.insertat(value)
            self.saveTofile(value,fn)

    def saveTofile(self,ele,fn):
            o=open(fn,'w')
            temp = self.head
            while (temp != None):
                ttemp = temp.data
                while (ttemp != None):
                    f = o.write(" " + str(ttemp.data))
                    ttemp = ttemp.next
                temp = temp.next
            o.close()

    def deletefromfile(self,prev,temp,hdata):
        tn = temp.next
        if prev==None:
            hdata.data=tn
        else:
          prev.next=tn

    def show(self):
        temp=self.head
        while(temp!=None):
                ttemp=temp.data
                while(ttemp!=None):
                    print(ttemp.data,end=" ")
                    ttemp=ttemp.next
                print()
                temp=temp.next
ll=LinkList()
try:
    fn, num = input("Enter the file name and the number to be searched\n eg hash.txt,3").split(",")
    num=int(num)
    o = open(fn, 'r')
    r = o.read()
    r=r.lstrip()
    store = ""
    for i in range(len(r)):
        if r[i] != " ":
            store = store + r[i]
        if r[i] == " " or i == len(r) - 1:
            v = int(store)
            ll.insertat(v)
            store = ""
    ll.find(num,fn)
    ll.show()
    o.close()
except Exception as e:
    print(e)








