import re,datetime
desc='''Hello <<name>>, we have your full name as <<full name>> in our system .
Your Contact number is 91-xxxxxxxxxx.Please ,let us know in case of 
any clarification  Thanks you BridgeLabz 01/01/2016'''

fullname=input("Enter your 'Full Name' ")
fname=""
lname=""
contact=""
date=""
# command=True
if re.search("\D{2,20}\s\D{2,20}",fullname):
     fname,lname=fullname.split(" ")
     desc=re.sub("<<name>>",str(fname),str(desc))
     desc = re.sub("<<full name>>", str(fullname), str(desc))
     mob= input("Enter the mobile number as '91-xxxxxxxxxx' ")
     if re.search("91-\d{10}",mob):
         desc = re.sub("91-xxxxxxxxxx", str(mob), str(desc))
         date=input("Enter date of enquiry")
         if re.search("\d{2}/\d{2}/\d{4}",date) :
             desc = re.sub("01/01/2016", str(date), str(desc))
             print(desc)
         else:
             print("Incorrect date formate")
     else:
         print("enter correct number")
else:
    print("Wrong input Name  \n      eg.  Prashant Jha ")





