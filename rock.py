from random import choice

def check(user,comp):
    
    check_dict = {'r':'s|smashes','s':'p|cuts','p':'r|covers','r':'l|crushes','l':'sp|poisons','sp':'s|smashes','s':'l|decapitates','l':'p|eats','p':'sp|disproves','sp':'r|vaporizes'}
    
    global user_score, comp_score
    
    
    for key in check_dict:
        val = check_dict[key].split("|")[0]
        msg = check_dict[key].split("|")[1]
        if key == user and val == comp:
            print("%s %s %s , you win" % (key , msg , val))
            
            user_score += 1
            break
            
        elif key == comp and val== user:
            print("%s %s %s , i win " %(key , msg , val) )
            
            comp_score += 1
            break
    else:
        print("Tie")
                  


print("Rock-Paper-Scissors\nBest of 5")
options = ['r','p','s','l','sp']
user_score = 0
comp_score = 0

for i in range(5):
    
    print("Options :\n1)Rock(r)\n2)Paper(p)\n3)Scissors(s)\n4)Lizard(l)\n5)Spock(sp)")
    user = input("Enter choice(r/p/s/l/sp) : ")
    
    if user not in options:
        print("Wrong choice")
        continue
    
    comp = choice(options)
    print("Computer chooses :",comp)
    check(user,comp)
    ch = input("Continue?(y/n)")
    
    if ch == 'n':
        break
    print("\n\n")
    
print("\nGame Exited")
if user_score > comp_score:
    print("You Win!!")
elif user_score < comp_score:
    print("I Win!!")
else:
    print("Its a tie!!")
print("My score :",comp_score)
print("Your score :",user_score)

    
    
