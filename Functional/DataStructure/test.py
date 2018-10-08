class BST:
    def __init__(self,n):
        self.st=[0]*n
        self.nt=n
        self.st[0]=1
        self.st[1]=2
    def noOfTree(self,n):
      print(self.st)
      sum=0
      if self.st[n-1] > 0:
        for i in range(n):
            for j in range(n):
              if i+j==n:
                print("value of i  "+str(i)+" value of j  "+str(j))
                e1=self.st[i]
                e2=self.st[j]
                print("value of e1 is "+str(e1))
                print("value of e2 is " + str(e2))
                sum=sum+e1*e2
                print("value of sum is "+str(sum))
      else:
          self.noOfTree(n-1)










num=int(input("Enter the number "))
BST(num).noOfTree(num-1)