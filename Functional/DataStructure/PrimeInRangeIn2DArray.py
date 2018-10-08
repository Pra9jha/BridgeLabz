def primeOrNot(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    else:
        return True

prime=[["0-100    :"],["100-200  :"],["200-300  :"],["300-400  :"],["400-500  :"],["500-600  :"],["600-700  :"],["700-800  :"],["800-900  :"],["900-1000 :"]]
for i in range(2,1000+1):
 if primeOrNot(i):
    prime[int(i/100)].append(i)
for i in range(len(prime)):
    for j in range(len(prime[i])):
        print(prime[i][j],end=" ")
    print()
