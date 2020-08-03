from random import randint

choices = ["rock", "paper", "scissors"]
Wins = 0
Losses = 0 
playerAnswer = False
alwaysWinReponse = "rock"

def counter_func():
    pluralwin = "s" if Wins > 1 else ""
    pluralloss = "es" if Losses > 1 else ""
    print("You have", Wins, "Win" + pluralwin, "and", Losses, "Loss" + pluralloss,".")

def alwaysWinning(answer):
        if answer == "rock":
            return "paper"
        elif answer == "paper":
            return "scissors"
        else:
            return "rock"

while playerAnswer == False:
    r = randint(0,2)
    # print("rand", r)
    playerAnswer = input("Rock, Paper, or Scissors? ")
    
    computer = alwaysWinning(playerAnswer)

    print("The computer chose",computer, "and you chose", playerAnswer)

    playerAnswer = playerAnswer.lower()
    if playerAnswer == computer:
        print("Tie!")
        counter_func()
    elif playerAnswer == "rock":
        if computer == "paper":
            print("You lose!", computer, "wraps", playerAnswer) 
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", playerAnswer, "crushes", computer)
            Wins = Wins + 1
            counter_func() 
    elif playerAnswer == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", playerAnswer)
            Losses = Losses + 1
            counter_func()  
        else: 
            print("You win!", playerAnswer, "wraps", computer)
            Wins = Wins + 1
            counter_func()   
    elif playerAnswer == "scissors":
        if computer == "rock":
            print("You lose!", computer, "crushes", playerAnswer)
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", playerAnswer, "cuts", computer)
            Wins = Wins + 1
            counter_func()  
    else:
        print("That's not a valid move. Check your spelling.")
    playerAnswer = False
    computer = choices[r]
      
    
        


        
        





   
