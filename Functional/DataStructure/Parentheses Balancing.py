'''
 **Purpose:We have to check either parentheses is balanced or not if
  the parentheses is not balanced then the expression cannot be solved
 **@author Prashant Kumar Jha
 **@since  14-09-2018
 here  math and random class is imported
'''

# class Stack is having members as empty list , a variable ,and method like push(),poop()
# isEmpty() , and peep()

class Stack:
    stack =[]
    top=-1
    # push() is to insert the element  to the stack method push is having two parameter
    # one is the self which refers to the address of the class and element will be
    # to be inserted to the stack  having the value

    def push(self,element):
       if self.top==-1:
           self.top=0
           self.stack.insert(self.top,element)
       else :
           self.top=self.top+1
           self.stack.insert(self.top,element)
    # poop() is to remover the top element from the stack it will and reset the top value
    # this method is having only one parameter self which refers to the object of the class

    def poop(self):
       if self.top!=-1:
           self.stack.remove(self.stack[self.top])
           self.top=self.top-1
       else:
           print("Under flow cannot be pooped")
    # peep() which returns the last element of the stack it is also having one
    # parameter self which refers to the object of the class
    def peep(self):
        if self.top != -1:
            # self.top = self.top - 1
            return self.stack[self.top]
        else:
            print("No element ")
    # isEmpty() returns boolean value if stack is empty it will
    # return true otherwise it will return false

    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    # show() is used to display the element present in our stack
    def show(self):
      itr=0
      while itr<=self.top:
         print(str(self.stack[itr]),end=" ")
         itr=itr+1
      print()
# we have created object of Stack class and store it to variable 's'
s=Stack()
# here we have taken an input i.e mathematical expression in string format
expression=input("Enter the expression")
# Logic to check parenthesis is balanced or not
for i in range(len(expression)):
  if s.isEmpty():
      if expression[i]=="(":
          s.push(expression[i])

      elif expression[i]==")":
          print("Parenthesis is Unbalanced")
          exit()
  elif not s.isEmpty():
      if expression[i]=="(":
          s.push(expression[i])

      elif expression[i]==")" and s.peep()=="(":
          s.poop()

if s.isEmpty():
    print("Parenthesis is balanced")
else:
    print("Parenthesis is unbalanced")

