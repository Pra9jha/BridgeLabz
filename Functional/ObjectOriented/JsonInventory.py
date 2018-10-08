import json
details={"Rice":[{"name":"Basmati","weight":"5kg","price":"40"},
                 {"name":"BrownRice","weight":"3kg","price":"135"},
                 {"name": "KOlam", "weight":"10kg", "price": "51"}
                ],
         "Pulse":[{"name": "Chana", "weight":"10kg", "price": "100"},
                  {"name": "Chana", "weight":"9kg", "price": "105"},
                  {"name": "KabuliChana", "weight": "5kg", "price": "110"}
                  ],
         "Wheat":[{"name":"Broken Wheat","weight":"20kg","price":"31"},
                  {"name":"Indian White Wheat ","weight":"10kg","price":"150"},
                  {"name":"Red Wheat Grain","weight":"50kg","price":"23"},
                ]
         }

o=open('RiceWheatPulseDetails.json','w')
json_string = json.dumps(details)
o.write(json_string)
o.close()

f=open('RiceWheatPulseDetails.json','r')
dataStore=json.load(f)

for k in range(len(dataStore)):
    if k==0:
        type="Rice"
    elif k==1:
        type="Wheat"
    elif k == 1:
        type = "Pulse"
    print("Different type of "+type+ " available ")
    for i in range(len(dataStore["Rice"])):
        print("type        :" + (dataStore[type][i]["name"]) + "\n")
        print("weight      :" + dataStore[type][i]["weight"] + "\n")
        print("price/kg    :" + dataStore[type][i]["price"] + "\n")
        tv = int(int(dataStore[type][i]["weight"][:-2]) * int(dataStore[type][i]["price"]))
        print("Total value of" + (dataStore[type][i]["name"]) + "rice is INR " + str(tv))
        print("-------------------------------------------------------------------------")


