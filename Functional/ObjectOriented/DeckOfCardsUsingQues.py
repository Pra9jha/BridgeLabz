import random
from ObjectOriented import QuesUsingLinkList
class Player:
    def arrange(self,deck):
        rank={"02":"2", "03":"3", "04":"4", "05":"5", "06":"6", "07":"7", "08":"8", "09":"9", "10":"10", "Ja":"11", "Qu":"12", "Ki":"13", "Ac":"1"}
        pl=[]
        for i in range(4):

            print(deck[i],end=" ")
        print()
        for i in range(4):
            if len(pl)==0:
                pl.insert(deck[i])
            else:
                pass







        #                    if int(rank[pl[0][-2:]])>int(val):#j==0:
        #                        print("into if val is " + str(j))
        #                        pl.insert(0, deck[i])
        #                        print("_________"+str(pl)+"________________")
        #                    elif int(rank[pl[j][-2:]])>=int(val):
        #                        print("into elif val is " + str(j))
        #                        pl.insert(i-1,deck[i])
        #                        print("_______" + str(pl) + "______________\n")
        #                    else:
        #                        print("into else val is " + str(j))
        #                        pl.append( deck[i])
        #                        print("_______" + str(pl) + "______________\n")
        #
        print("\n________________________")
        print(pl)




















class Main:
 suit=["{Clubs}:", "{Diamonds}:", "{Hearts}:", "{Spades}:"]
 rank=["02", "03", "04", "05", "06", "07", "08", "09", "10", "Ja", "Qu", "Ki", "Ac"]
 deck=[]
 for i in range(len(suit)):
     for j in range(len(rank)):
         deck.append(suit[i] + "" + rank[j])
 random.shuffle(deck)
 Player().arrange(deck)

