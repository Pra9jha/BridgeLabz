class dQueue:
    que = []
    front = -1
    rear = -1
    def addrear(self, element):
        if self.front == -1 and self.rear == -1:
            self.rear = 0
            self.front = 0
            self.que.insert(self.rear, element)
        else:
            self.rear = self.rear + 1
            self.que.insert(self.rear, element)

    def removefront(self):
        self.front = self.front + 1
        if self.size() >= 0:
            return self.que[self.front - 1]
        else:
            return "No more element to be pooped "
    def removerear(self):
        self.rear=self.rear-1
        if self.size()>=0:
            return self.que[self.rear+1]
        else:
            return "No more element to be pooped "

    def size(self):

        if self.front == -1 and self.rear == -1:
            return -1
        else:
            return (self.rear - self.front) + 1

    def show(self):
      if self.front !=-1 and self.rear!=-1:
        for i in range(self.front, self.rear + 1):
            print(self.que[i], end=" ")
        print()
d=dQueue()
word=input("Enter the word to be checked")
for i in range(len(word)):
    d.addrear(word[i])
for i in range(int(len(word)/2)) :
  if d.removerear()!=d.removefront():
      print("Not a palindrome")
      exit()
print("Is a palindrome")





