import json

class company:
    def display(self,command):
        f = open('stock.json', 'r')
        data = json.load(f)
        if command == 1:
            for i in data["stock"]:
                print("Company_Name      "+str(data["stock"][i]["name"]))
                print("No of Share       "+str(data["stock"][i]["share"]))
                print("price             "+str(data["stock"][i]["price"]))
                print("Total share value "+str(int(data["stock"][i]["share"])*int(data["stock"][i]["price"])))
                print("_______________________________")
        else:
               c_name= input("Enter the name of the company")
               print("Company_Name      " + str(data["stock"][c_name]["name"]))
               print("No of Share       " + str(data["stock"][c_name]["share"]))
               print("price             " + str(data["stock"][c_name]["price"]))
               print("Total share value " + str(int(data["stock"][c_name]["share"]) * int(data["stock"][c_name]["price"])))


           # print(str(data["stock"][c_name]))

class Main:
    command=int(input("Enter 1 to show all the details\nEnter 2"
                      " to Show the details of specific comapnay"))

    company().display(command)

