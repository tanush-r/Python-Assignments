import random

def guess():
    while True:
        g = int(input("Enter the guess limit : "))
        if g >= 1:
            print("Ok, limit is",g)
            return g
        else:
            print("Too low")

def check_range(start,end):
    if start >= end:
        return False
    else:
        return True

def check_guess(start,end):
    while True:
        guess = int(input("Enter you guess : "))
        if start <= guess <= end:
            return guess
        else:
            print("Not in range")


    

print("Guess the number game!\n")

limit = guess()
start = end = 0
running = True
while True:
    start = int(input("Enter start num : "))
    end = int(input("Enter end num : "))
    if check_range(start,end):
        break
    else:
        print("Wrong range")

ans = random.randint(start,end)

print("Lets begin the game!!\n\n")
print("____________________________________________")

for i in range(limit):
    guess = check_guess(start,end)
    if guess == ans:
        print("You win!!!\nYou took %d chances" % (i+1))
        break
    elif guess < ans:
        print("Too low")
    else:
        print("Too high")
else:
    print("You ran out of chances!")
    


    
    

