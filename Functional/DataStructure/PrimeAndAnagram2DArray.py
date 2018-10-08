''''
 **Purpose: To find prime number in the range of 1 to 1000 and if the 
   number is anagram then store it in the 2D list such that first dimention shows 
   the range and the second dimention shows the number lying in that range
 **@author Prashant Kumar Jha
 **@since  14-09-2018
'''''

# the method primeOrNot checks either the number is prime it takes one argument oi.e num
# if the number is prime then it return True and if the number is

def primeOrNot(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    else:
        return True
def angramOrNot(num1,num2):
    if sorted(num1)==sorted(num2):
        return True
    else:
       return False

prime=[]
pa=[["0-100    :"],["100-200  :"],["200-300  :"],["300-400  :"],["400-500  :"],["500-600  :"],["600-700  :"],["700-800  :"],["800-900  :"],["900-1000 :"]]
pna=[["0-100    :"],["100-200  :"],["200-300  :"],["300-400  :"],["400-500  :"],["500-600  :"],["600-700  :"],["700-800  :"],["800-900  :"],["900-1000 :"]]
for i in range(2,1000+1):
 if primeOrNot(i):
    prime.append(i)

for i in range(len(prime)):
    for j in range(len(prime)):
        if angramOrNot(str(prime[i]),str(prime[j])) and i!=j:
           pa[int(prime[i]/100)].append(prime[i])
           break

for i in range(len(pa)):
    for j in range(len(pa[i])):
        print(pa[i][j],end=" ")
    print()

