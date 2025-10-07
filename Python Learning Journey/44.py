a=int(input("Enter 1 to play with friend and 2 to play with bot:"))
if(a==2):
    
    # using random module
    import random
    def check(comp,user):
        if(comp==user):
            return 0
            
        if(comp==0 and user==1):
            return -1
        
        if(comp==1 and user==2):
            return -1
            
        if(comp==2 and user==0):
            return -1
            
        return 1
        
    comp = random.randint(0,2)
    user=int(input("0 for snake, 1 for water, 2 for gun\n"))
    
    score=check(comp,user)
    print("You",user)
    print("Computer",comp)
    if(score==0):
        print("Its draw.")
        
    elif(score==1):
        print("You win")
        
    else:
        print("You lose")
        
    
    
        
        
else:
        
    # snake water gun
    scoreofplayer1=0
    scoreofplayer2=0
    for tose in range(5):
    
        p1=int(input("Enter your choise p1.0 for snake, 1 for water, 2 for gun\n"))
        p2=int(input("Enter our choise p2.0 for snake, 1 for water, 2 for gun\n"))
    
        if(p1==2):
            if(p2==0):
                print("p1 win")
                scoreofplayer1 += 1
            elif(p2==1):
                print("p2 win")
                scoreofplayer2+=1
            else:
                print("Tie")
    
        elif(p1==0):
            if(p2==1):
                print("p1 win")
                scoreofplayer1+=1
            elif(p2==2):
                print("p2 win")
                scoreofplayer2+=1
            else:
                print("Tie")
    
        else:
            if(p2==2):
                print("p1 win")
                scoreofplayer1+=1
            elif(p2==0):
                print("p2 win")
                scoreofplayer2+=1
            else:
                print("Tie")
                
    print("player1 score is:",scoreofplayer1 )
    print("player2 score is:",scoreofplayer2 )
    
        
