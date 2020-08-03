from random import randint

choices = ["rock", "paper", "scissors"]
Wins = 0
Losses = 0 
player = False

def counter_func():
    pluralwin = "s" if Wins > 1 else ""
    pluralloss = "es" if Losses > 1 else ""
    print("You have", Wins, "Win" + pluralwin, "and", Losses, "Loss" + pluralloss,".")

while player == False:
    r = randint(0,2)
    # print("rand", r)
    computer = choices[r]
    player = input("Rock, Paper, or Scissors? ")
    print("The computer chose",computer, "and you chose", player)
    player = player.lower()
    if player == computer:
        print("Tie!")
        counter_func()
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "wraps", player) 
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", player, "crushes", computer)
            Wins = Wins + 1
            counter_func() 
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
            Losses = Losses + 1
            counter_func()  
        else: 
            print("You win!", player, "wraps", computer)
            Wins = Wins + 1
            counter_func()   
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "crushes", player)
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", player, "cuts", computer)
            Wins = Wins + 1
            counter_func()  
    else:
        print("That's not a valid move. Check your spelling.")
    player = False
    computer = choices[r]
      
    
        


        
        





   
