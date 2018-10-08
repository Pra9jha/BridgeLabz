class Queue:
     que=[]
     withdraw=0
     deposit=0
     front=-1
     rear=-1
     def __init__(self,bankBalance):
         self.bankBalance=bankBalance
     def enqueue(self,element,purpose,amount):
         if self.front==-1 and self.rear==-1:
             self.rear=0
             self.front=0
             self.que.insert(self.rear,element)
         else:
             self.rear=self.rear+1
             self.que.insert(self.rear,element)
         if purpose=='w':
             self.withdraw=self.withdraw+amount
             self.bankBalance=self.bankBalance-amount
             # print("current bank balance is "+str(self.bankBalance))
         elif purpose=='d':
             self.deposit=self.deposit+amount
             self.bankBalance=self.bankBalance+amount
             # print("current bank balance is " + str(self.bankBalance))

     def deque(self):
          self.front=self.front+1
          if self.size() >=0:
             return self.que[self.front-1]
          else:
              return "No more person is left "
     def size(self):

          if self.front==-1 and self.rear==-1:
              return -1
          else:
            return (self.rear-self.front)+1
     def show(self):
          for i in range(self.front ,self.rear+1) :
            print(self.que[i],end=" ")
            print()

bb=int(input("Enter total balance of bank"))
q=Queue(bb)
while True:
  person = input("Enter the Person to the que if all person is added click 'done'::\t")
  if person!='done':
   purpose = input("Enter 'w' to withdraw and 'd' to deposit::\t")
   amount = int(input("Enter amount ::\t"))
  if person=='done':
      while q.size()>0:
          print(q.deque())
      print("Withdraw is " + str(q.withdraw))
      print("Deposit is " + str(q.deposit))
      print("BankBalance is "+str(q.bankBalance))
      exit()
  else :
      if purpose=='w' and q.bankBalance-amount>=0 or purpose=='d':
            q.enqueue(person,purpose,amount)
      else:
          print("Insufficient amount in the cash counter")



