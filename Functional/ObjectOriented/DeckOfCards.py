import random
suit=["Clubs", "Diamonds", "Hearts", "Spades"]
rank=["[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[10]", "[Jack]", "[Queen]", "[King]", "[Ace]"]
deck=[]
for i in range(len(suit)):
    for j in range(len(rank)):
        deck.append(suit[i]+""+rank[j])
random.shuffle(deck)
player=[["player1  :-"],["player2  :-"],["player3  :-"],["player4  :-"]]
for i in range(36):
    player[int(i/9)].append(deck[i])

for i in range(len(player)):
    for j in range(len(player[i])):
        print(player[i][j],end="  ")
        if j%3==0 and j!=0:
            print("\n\t\t\t",end=" ")

    print("\n")

