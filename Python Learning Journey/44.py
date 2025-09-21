# snake water gun
scoreofplayer1=0
scoreofplayer2=0
for tose in range(5):

    p1=input("Enter your choise p1.")
    p2=input("Enter our choise p2.")

    if(p1=='Gun'):
        if(p2=='Snake'):
            print("p1 win")
            scoreofplayer1 += 1
        else:
            print("p2 win")
            scoreofplayer2+=1

    elif(p1=='Snake'):
        if(p2=='Water'):
            print("p1 win")
            scoreofplayer1+=1
        else:
            print("p2 win")
            scoreofplayer2+=1

    else:
        if(p2=='Gun'):
            print("p1 win")
            scoreofplayer1+=1
        else:
            print("p2 win")
            scoreofplayer2+=1
print("player1 score is:",scoreofplayer1 )
print("player2 score is:",scoreofplayer2 )

    




