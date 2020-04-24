import random

def scoreboard_ini():
    playerno = int(input("Enter no of players : "))
    scoreboard = dict()
        
    for num in range(playerno):
        playername = input("Enter name of player %d : "%(num+1))
        scoreboard[playername] = 0
    return scoreboard


def welcome(scoreboard):
    print("\nThe players are : ",end = "")     
    for player in scoreboard.keys():
        print(player,end=" ,")
    print("\nWelcome to the game, players!\n")


def display_scoreboard(scoreboard):
    print("\n--------------Scoreboard-------------------")
    for player in scoreboard:
        print("%s : %d" % (player,scoreboard[player]))


def main_game(scoreboard):
    gameRunning = True#check variable
    while gameRunning == True: #game loop
            
            display_scoreboard(scoreboard)
            print("\n")
            for player in scoreboard:
                ch = input(player+", Do you want to play? (y/n) : ")
                
                if ch == "n":
                    print("Ok. You are skipping your chance \n")
                    continue
                num = random.randint(mini,maxi)
                print("The number rolled by the dice is",num)
                scoreboard[player] += num
                print("Your score has been updated \n")
                
                if scoreboard[player] >= 30:
                    print("\n\nGame Over! The Winner is",player)
                    display_scoreboard(scoreboard)
                    gameRunning = False
                    break
                print("\n")
    gameRunning = True

#main program
print("Digital dice \n\n")
mini = 1
maxi = 6


while True: #main loop
        
        ch = input("Do you want to play?(y/n) : ")
        
        if ch == "n":
            print("Okay bye!")
            break
        
        elif ch == "y":
            print("Continue\n\n")
            
        scoreboard = scoreboard_ini()
        welcome(scoreboard)
        main_game(scoreboard)
        
       
