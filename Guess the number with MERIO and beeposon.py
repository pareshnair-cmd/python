import random
import time
number = random.randint(1,100)
def intro():
    print ("Buddy, lets play a game, guess the number from 1 to 100")
    if (number%2==0):
        x = 'even'
    else:
        x ='odd'
    print  ("\nThis number is an {} number".format(x))
    time.sleep(0.5)
    print ("start")

def pick():
    guesstaken = 0
    while guesstaken < 6:
        time.sleep(0.25)
        enter = input("guess: ")
        try:
            guess = int(enter)
            if guess <= 100 and guess >= 1:
                guesstaken = guesstaken+1
                if guesstaken < 6:
                    if guess < number:
                        print ("<Higher>")
                    if guess  > number:
                        print ("<lower>")
                    if guess != number:
                        time.sleep(0.5)
                        print("<TRY_again>")
                    if guess == number:
                        print ("<CorrecT>")
                        break
            if guess >=100 or guess <= 1:
                print ("Ugh,your not funny")
                time.sleep(.25)
                print ("try again with the followin CONDITIONS: 1 - 100")
        except:
            print (enter+"Aint a number dingushead")
    if guess == number:
        guesstaken = str(guesstaken)
        print ("CONGRATUALATIONS MY BIGGY CHUNGUS WHOPPERINO ITS CORRECT!!!")
    if guess != number:
        print ("NO, it was" + str(number))    
playagain = "yes"    
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print ("Wanna try AGAIN")
    playagain = input()
