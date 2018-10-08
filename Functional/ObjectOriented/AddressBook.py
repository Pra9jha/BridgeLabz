import json,re
class AddressBook:
    def openFie(self):
        f=open('AddressBook.json','r')
        ab_data=json.load(f)
        return ab_data
    def writeToFile(self,data):
        f = open('AddressBook.json', 'w')
        dum=json.dumps(data)
        f.write(dum)
    def writeinBook(self,fname,lname,city,state,phone):
         data=self.openFie()
         data["contact"].append({"first_Name":fname,"last_Name":lname,"city_Name":city,"stat_name":state,"Phone_Number":phone})
         print(data)
         self.writeToFile(data)
    def editInformation(self,c,fname,prev,curr):
        data = self.openFie()
        flag=0
        for i in range(len(data["contact"])):
            print(data["contact"][i]["first_Name"])
            if data["contact"][i]["first_Name"]==fname:

                if c==str(1) and data["contact"][i]["city_Name"] == prev:
                    data["contact"][i]["city_Name"]=curr
                    flag=1

                elif c == str(2) and data["contact"][i]["stat_name"] == prev:
                    data["contact"][i]["stat_name"] = curr
                    flag = 1

                elif c == str(3) and data["contact"][i]["Phone_Number"] == prev:
                    data["contact"][i]["Phone_Number"] = curr
                    flag = 1
            elif flag==0:
                print("Wrong input")
        print(data)















class Main:
  # try:
    ab = AddressBook()
    print(ab.openFie())
    command = int(input("Enter 1 to Add new Person\nEnter 2 to Edit the saved data\nEnter 3 to search Information"))
    if command==1:
      fname="";lname="";city="";state="";phone=""
      fullname = input("Enter full name separated by space\t")
      if re.search("\D{2,20}\s\D{2,20}", fullname):
          fname, lname = fullname.split(" ")
          city_state = input("Enter city name and state name separated by space\t")
          if re.search("\D{2,20}\s\D{2,20}", city_state):
              city, state = city_state.split(" ")
              phone = input("Enter phone number\t")
              if re.search("\d{10}", phone):
                  pass
              else:
                  print("Incorrect mobile number")
                  exit()
          else:
              print("Naming convention should b followed")
              exit()
      else:
          print("Naming convention should b followed")
          exit()
      ab.writeinBook(fname,lname,city,state,phone)
    elif command==2:
        fname=input("Enter first name of the person whose data is to be edited \t")
        c=input("Press   1 :'City _Name'\n\t\t2 : State_Name\n\t\t3 : Phone_Number")
        prev=input("Enter Previous saved data ")
        curr=input("Enter current information ")
        if re.search("\D{2,20}}", fname) :
          ab.editInformation(c,fname,prev,curr)
        else:
            print("Naming Convention should be m")

  # except Exception as e:
  #     print(e)
