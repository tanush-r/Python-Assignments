print("Python Quiz Game \n\n")
score = 0
s = input("1) How to compare the values of 2 variables?")
if(s == "x==y"):
    score += 1
    print("Correct!")
else:
    print("Wrong")
s = input("2) Value of (true and true)")
if(s == "true"):
    score += 1
    print("Correct!")
else:
    print("Wrong")
s = input("3) 17 < 12 and 2 > 3")
if(s == "false"):
    score += 1
    print("Correct!")
else:
    print("Wrong")
s = input("4) 10 + 2 == 12")
if(s == "true"):
    score += 1
    print("Correct!")
else:
    print("Wrong")

print("Quiz is over")
if score >= 3:
    print("You win")
else:
    print("You lose")

