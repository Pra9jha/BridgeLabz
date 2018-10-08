class BST:
    st = [0] * 10
    st[0]=1;st[1]=1
    def __init__(self,n):
        self.save=n


    def noOfTree(self,n):
        sum=0
        if self.st[n] > 0:
            for i in range(n + 1):
                for j in range(n + 1):
                    if i + j == n :
                        print(str(i) + "  " + str(j))
                        e1 = self.st[i]
                        print("value of e1    "+str(e1))
                        e2 = self.st[j]
                        print("value of e2    " + str(e2))
                        sum = sum + e1 * e2
                        print(sum)
            self.st.insert(n+1,sum)

        else:
            self.noOfTree(n - 1)
        print(self.st)

print(BST(5).noOfTree(5))
