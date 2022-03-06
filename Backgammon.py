#Backgammon
import random
#startin board
board = [["0","1","2","3","4","5","6","7","8","9","10/0tb"],
         ["r"," "," "," ","b"," ","b"," "," ","r","1"],
         ["r"," "," "," ","b"," ","b"," "," ","r","2"],
         [" "," "," "," ","b"," ","b"," "," ","r","3"],
         [" "," "," "," ","b"," "," "," "," ","r","4"],
         [" "," "," "," ","b"," "," "," "," ","r","5"],
         [" "," "," "," "," "," "," "," "," "," ","6"],
         [" "," "," "," "," "," "," "," "," "," ","7"],
         [" "," "," "," "," "," "," "," "," "," ","8"],
         [" "," "," "," "," "," "," "," "," "," ","9"],
         [" "," "," "," "," "," "," "," "," "," ","10"],
         [" "," "," "," "," "," "," "," "," "," ","11"],
         [" "," "," "," "," "," "," "," "," "," ","12"],
         [" "," "," "," "," "," "," "," "," "," ","13"],
         [" "," "," "," ","r"," "," "," "," ","b","14"],
         [" "," "," "," ","r"," "," "," "," ","b","15"],
         [" "," "," "," ","r"," ","r"," "," ","b","16"],
         ["b"," "," "," ","r"," ","r"," "," ","b","17"],
         ["b"," "," "," ","r"," ","r"," "," ","b","18"],
         ["0","1","2","3","4","5","6","7","8","9","10/19tr"]]

#print board
def printboard():
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print(board[7])
    print(board[8])
    print(board[9])
    print(board[10])
    print(board[11])
    print(board[12])
    print(board[13])
    print(board[14])
    print(board[15])
    print(board[16])
    print(board[17])
    print(board[18])
    print(board[19])

def throwdice():
    return random.randint(1,6)

def score(dicea,diceb):
    if dicea == diceb:
        return 4*dicea
    else:
        return dicea + diceb
score1=0
score2=0
turn=0
taken1=0
taken2=0
while score1==score2:
    dicea = throwdice()
    diceb = throwdice()
    score1 = score(dicea,diceb)
    
    print("Player1 throws:",dicea,diceb)
    
    dicea = throwdice()
    diceb = throwdice()
    score2 = score(dicea,diceb)

    print("Player2 throws:",dicea,diceb)

    if score1>score2:
        print("Player 1 starts the game")
        turn=1
    elif score2>score1:
        print("Player 2 starts the game")
        turn=2

while taken1<15 and taken2<15:

    printboard()

    if turn==1:
        print("Player 1's turn. (reds)")
        dicea=throwdice()
        diceb=throwdice()
        print("Player 1 throws:",dicea,diceb)
        if dicea==diceb:
            move1startx=int(input("select starting point x for move 1:"))
            move1starty=int(input("select starting point y for move 1:"))
            board[move1starty][move1startx]=" "

            printboard()
            
            move1endx=int(input("select ending point x for move 1:"))
            move1endy=int(input("select ending point y for move 1:"))
            board[move1endy][move1endx]="r"

            if(move1endy==19)and(move1endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break

            printboard()
            
                  
            move2startx=int(input("select starting point x for move 2:"))
            move2starty=int(input("select starting point y for move 2:"))
            board[move2starty][move2startx]=" "

            printboard()
            
            move2endx=int(input("select ending point x for move 2:"))
            move2endy=int(input("select ending point y for move 2:"))
            board[move2endy][move2endx]="r"

            if(move2endy==19)and(move2endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break

            printboard()
            
            move3startx=int(input("select starting point x for move 3:"))
            move3starty=int(input("select starting point y for move 3:"))
            board[move3starty][move3startx]=" "

            printboard()
            
            move3endx=int(input("select ending point x for move 3:"))
            move3endy=int(input("select ending point y for move 3:"))
            board[move3endy][move3endx]="r"
            
            if(move3endy==19)and(move3endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break

            printboard()

            move4startx=int(input("select starting point x for move 4:"))
            move4starty=int(input("select starting point y for move 4:"))
            board[move4starty][move1startx]=" "

            printboard()
            
            move4endx=int(input("select ending point x for move 4:"))
            move4endy=int(input("select ending point y for move 4:"))
            board[move1endy][move1endx]="r"

            if(move4endy==19)and(move4endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break

            printboard()

            turn = 2
        else:
            move1startx=int(input("select starting point x for move 1:"))
            move1starty=int(input("select starting point y for move 1:"))
            board[move1starty][move1startx]=" "

            printboard()
            
            move1endx=int(input("select ending point x for move 1:"))
            move1endy=int(input("select ending point y for move 1:"))
            board[move1endy][move1endx]="r"
            
            if(move1endy==19)and(move1endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break

            printboard()
                  
            move2startx=int(input("select starting point x for move 2:"))
            move2starty=int(input("select starting point y for move 2:"))
            board[move2starty][move2startx]=" "

            printboard()
            
            move2endx=int(input("select ending point x for move 2:"))
            move2endy=int(input("select ending point y for move 2:"))
            board[move2endy][move2endx]="r"

            if(move2endy==19)and(move2endx==10):
                taken1+=1
                board[move1endy][move1endx]=taken1
                if taken1 >= 15:
                    print("Player 1 wins !!!")
                    break
                
            printboard()
            
            turn=2
            
            skip=True
                  
    else:
        print("Player 2's turn. (blacks)")
        dicea=throwdice()
        diceb=throwdice()
        print("Player 2 throws:",dicea,diceb)
        if dicea==diceb:
            move1startx=int(input("select starting point x for move 1:"))
            move1starty=int(input("select starting point y for move 1:"))
            board[move1starty][move1startx]=" "
            
            printboard()
            
            move1endx=int(input("select ending point x for move 1:"))
            move1endy=int(input("select ending point y for move 1:"))
            board[move1endy][move1endx]="b"

            if(move1endy==0)and(move1endx==10):
                taken2+=1
                board[move1endy][move1endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
            
            move2startx=int(input("select starting point x for move 2:"))
            move2starty=int(input("select starting point y for move 2:"))
            board[move2starty][move2startx]=" "
            
            printboard()

            move2endx=int(input("select ending point x for move 2:"))
            move2endy=int(input("select ending point y for move 2:"))
            board[move2endy][move2endx]="b"

            if(move2endy==0)and(move2endx==10):
                taken2+=1
                board[move2endy][move2endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
            
            move3startx=int(input("select starting point x for move 3:"))
            move3starty=int(input("select starting point y for move 3:"))
            board[move3starty][move3startx]=" "

            printboard()
            
            move3endx=int(input("select ending point x for move 3:"))
            move3endy=int(input("select ending point y for move 3:"))
            board[move3endy][move3endx]="b"

            if(move3endy==0)and(move3endx==10):
                taken2+=1
                board[move3endy][move3endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
            

            move4startx=int(input("select starting point x for move 4:"))
            move4starty=int(input("select starting point y for move 4:"))
            board[move4starty][move1startx]=" "

            printboard()
            
            move4endx=int(input("select ending point x for move 4:"))
            move4endy=int(input("select ending point y for move 4:"))
            board[move1endy][move1endx]="b"

            if(move4endy==0)and(move4endx==10):
                taken2+=1
                board[move4endy][move4endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
            
            turn = 1
        else:
            move1startx=int(input("select starting point x for move 1:"))
            move1starty=int(input("select starting point y for move 1:"))
            board[move1starty][move1startx]=" "

            printboard()
            
            move1endx=int(input("select ending point x for move 1:"))
            move1endy=int(input("select ending point y for move 1:"))
            board[move1endy][move1endx]="b"

            if(move1endy==0)and(move1endx==10):
                taken2+=1
                board[move1endy][move1endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
                  
            move2startx=int(input("select starting point x for move 2:"))
            move2starty=int(input("select starting point y for move 2:"))
            board[move2starty][move2startx]=" "

            printboard()
            
            move2endx=int(input("select ending point x for move 2:"))
            move2endy=int(input("select ending point y for move 2:"))
            board[move2endy][move2endx]="b"

            if(move2endy==0)and(move2endx==10):
                taken2+=1
                board[move2endy][move2endx]=taken2
                if taken2 >= 15:
                    print("Player 2 wins !!!")
                    break
                
            printboard()
            
            turn=1

input("Thanks for playing !!!Press enter to quit...!!!     :  -   ) ")
