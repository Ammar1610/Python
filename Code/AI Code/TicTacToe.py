def grid():
    zero="X" if xstate[0] else ("0" if Ostate[0] else 0)
    one="X" if xstate[1] else ("O" if Ostate[1] else 1)
    two="X" if xstate[2] else ("O" if Ostate[2] else 2)
    three="X" if xstate[3] else ("0" if Ostate[3] else 3 ) 
    four="X" if xstate [4] else ("0" if Ostate[4] else 4)
    five="X" if xstate[5] else ("0" if Ostate[5] else 5)
    six="X" if xstate[6] else ("0" if Ostate[6] else 6) 
    seven="X" if xstate[7] else ("0" if Ostate[7] else 7)
    eight="X" if xstate[8] else ("O" if Ostate[8] else 8)

    print(f"{zero}|{one}|{two}")
    print("------")
    print(f"{three}|{four}|{five}")
    print("------") 
    print(f"{six}|{seven}|{eight}")

def sum(x,y,z):
        return x+y+z

def GoalState(xstate,Ostate):
    final=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in final:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("Player 1 Won!!")
            return 0
        elif(sum(Ostate[win[0]],Ostate[win[1]],Ostate[win[2]])==3):
            print("Player 2 Won!!")
            return 1
    return -1

xstate=[0,0,0,0,0,0,0,0,0]
Ostate=[0,0,0,0,0,0,0,0,0]
turn=1
while(True):
    grid()
    if(turn==1):
        print("Player 1") 
        val=int(input("Enter Index for X:"))
        xstate[val]=1
    else:
        print("Player 2:")
        val=int(input("Enter Index for 0:"))
        Ostate[val]=1
    GS=GoalState(xstate,Ostate)
    if(GS!=-1):
        print("Match Over")   
        grid()
        break 
    turn=1-turn

