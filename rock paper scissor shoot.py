import random
options = ["Rock","Paper","Scissors"]
comp = random.choice(options)
userchoice = str(input("rock,paper,scissor choose: "))
print ("you chose:"(userchoice))
print ("computer chose"(comp))
if userchoice == comp:
    print("Its a DRAW")
elif userchoice == "Rock" and comp == "Paper" or userchoice == "Scissors" and comp == "Rock" or userchoice == "Paper" and comp == "Scissors":
    print ("Computer wins...")
elif userchoice == "Paper" and comp == "Rock" or userchoice == "Rock" and comp == "Scissors" or userchoice == "Scissors" and comp == "Paper":
    print ("YOU WIN :D")