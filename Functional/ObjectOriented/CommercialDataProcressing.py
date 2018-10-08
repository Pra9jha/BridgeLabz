import json, datetime
from ObjectOriented import QuesUsingLinkList
class Company_panel:
    o = open('commDataProc.json', 'r')
    details=json.load(o)
    op = open('Customer.json', 'r')
    p_data = json.load(op)
    def createStockAccount(self,c_name,c_share,s_price,s_date,s_time):
      for i in self.details["stock"]:
          if i["name"]==c_name :
              comm=int(input("\nYour company is already registered\nPress 1 to go to previous menue Press Enter To exit "))
              if comm==1:
                 Main().command()
              else:
                  exit()
      else:
          print("into else")
          self.details["stock"].append({"name": c_name, "share": c_share, "price": s_price, "date": s_date, "time": s_time})
          self.writeToFile('commDataProc.json',self.details)
    def updateData(self,c_name,comm,val):
        for i in self.details["stock"]:
           if i["name"] == c_name:
               i[comm]=val
               break
        else:
            print("your company is not registered")
        self.writeToFile('commDataProc.json',self.details)
        if (input("Enter y to go to previous menue ") == "y"):
            Main().command()
    def remove(self,c_name):
        for i in self.details["stock"]:
            if i["name"]==c_name:
                self.details["stock"].remove(i)
        self.writeToFile('commDataProc.json', self.details)

    def writeToFile(self, fn, details):
        o = open(fn, 'w')
        json_string = json.dumps(details)
        o.write(json_string)

class Customer_Panel:
    o = open('commDataProc.json', 'r')
    details = json.load(o)
    op = open('Customer.json', 'r')
    p_data = json.load(op)

    def buyShare(self,p_name,c_name,n_share):
        for i in self.details["stock"]:
            if i["name"]==c_name and int(i["share"])>=int(n_share):
                i["share"]=int(i["share"])-int(n_share)
                self.writeToFile('commDataProc.json',self.details)
                self.p_data["customer"].append({"name":p_name,"c_name":c_name,"s_purchased":n_share,"dateTime":str(datetime.datetime.now()),"amt":int(n_share)*int(int(i["price"]))})
                self.writeToFile('Customer.json',self.p_data)
                break
        else:
            print("Invalid input view Company details properly")
        if (input("Enter y to go to previous menue ") == "y"):
            Main().command()
    def display_Cdetails(self,c_name):
        for i in self.details["stock"]:
            if i["name"]==c_name:
                print("Company        :"+i["name"] +"\nNo. of share   :"+str(i["share"])+"\nPrice of share :"+str(i["price"]))
                print("Posted on      :"+str(i["date"])+" "+str(i["time"]))
        if(input("Enter y to go to previous menue ") == "y"):
            Main().command()

    def writeToFile(self, fn, details):
        o = open(fn, 'w')
        json_string = json.dumps(details)
        o.write(json_string)

class MonitourInstitution:
    o = open('commDataProc.json', 'r')
    details = json.load(o)
    op = open('Customer.json', 'r')
    p_data = json.load(op)
    def display_Cdetails(self,c_name):
        for i in self.details["stock"]:
            if i["name"]==c_name:
                print("Company        :"+i["name"] +"\nNo. of share   :"+str(i["share"])+"\nPrice of share :"+str(i["price"]))
                self.valueOf(c_name)
                print("Posted on      :"+str(i["date"])+" "+str(i["time"]))
        if (input("Enter y to go to previous menue ") == "y"):
            Main().command()

    def p_details(self,p_name):
        print("Customer Name           :" + str(p_name))
        print("*********************************************")
        for j in self.p_data["customer"]:
            print("____________________________________________")
            if j["name"]==p_name:
                print("\nInversted in Company    :"+str(j["c_name"])+"\nNo. of share purchased  :"+str(j["s_purchased"])+"\nTotal amount invested   :"+str(j["amt"]))
                print("Date and time of deal :"+str(j["dateTime"]))
        if (input("Enter y to go to previous menue ") == "y"):
            Main().command()
    def valueOf(self,c_name):
        for i in self.details["stock"]:
          if i["name"]==c_name:
              print("Total share value of the company is "+str(int(i["share"])*int(i["price"])))
        if (input("Enter y to go to previous menue ") == "y"):
            Main().command()
    def trandetails(self):
        q=QuesUsingLinkList.Queue()
        for i in range(len(self.p_data["customer"])):
            q.enqueue(self.p_data["customer"][i])
        while q.size()>0:
            ele=q.dequeue()
            print(str(ele["name"])+"   :"+str(ele["amt"])+"   :"+str(ele["dateTime"]))

class Main:
  def command(self):
     com=input("If you represent Company press 'c', if you represent financial Institution,press'f', else press p to want to buy share\n    ")
     if com=='c':
         cp = Company_panel()
         command = int(input("Press 1 to upload your stock information\nPress 2 to update data of the company share or price\nPress 3 to delete share information      "))
         if command==1:
            c_name = str(input("Enter your company name   "))
            c_share = input("Enter number of share you want to sell   ")
            s_price = input("Enter price of each share    ")
            s_date, s_time = str(datetime.datetime.now()).split(" ")
            cp.createStockAccount(c_name, c_share, s_price, s_date, s_time)
         elif command==2:
            c_name=input("Enter your company name   ")
            comm,val = input("Write ('share',no. of share) if you want to update share   eg share,45 \nwrite ('price',price of each share) to update price   eg price,4566    ").split(",")
            if comm=="share" or comm=="price":
               cp.updateData(c_name, comm, val)
            else:
               print("Wrong input")
         elif command==3:
             c_name = input("Enter your company name   ")
             cp.remove(c_name)

     elif com=='p':
         cuspnl=Customer_Panel()
         command=int(input("Press 1 if you want to view company with its share chart and price\nPress 2 If you want to buy share      "))
         if command==1:
            c_name = str(input("Enter your company name     "))
            cuspnl.display_Cdetails(c_name)
         elif command==2:
            p_name = str(input("Enter your name   "))
            c_name = str(input("Enter company name   "))
            n_share = int(input("Entre number of share you want to buy   "))
            cuspnl.buyShare(p_name, c_name, n_share)
     elif com=='f':
         fm=MonitourInstitution()
         command=int(input("Press 1 if you want to Monitor company with its share chart and price\nPress 2 if you want to know compnay share value\nPress 3 to view customer details \nPress 4 to see transation details "))
         if command == 1:
            c_name = str(input("Enter company name    "))
            fm.display_Cdetails(c_name)
         elif command==2:
             c_name = str(input("Enter your company name    "))
             fm.valueOf(c_name)
         elif command==3:
           p_name=input("Enter the name of the customer    ")
           fm.p_details(p_name)
         elif command==4:
            fm.trandetails()


Main().command()