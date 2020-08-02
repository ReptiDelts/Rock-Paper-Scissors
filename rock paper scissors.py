from random import randint

choices = ["Rock", "Paper", "Scissors"]
Wins = 0
Losses = 0 

def counter_func():
    if 1 == Wins and 1 == Losses: 
        print("You have", Win, "Win and", Losses, "Loss.")
    elif 1 == Losses:
        print("You have", Wins, "Wins and", Losses, "Loss.")
    elif 1 == Wins:
        print("You have", Wins, "Win and", Losses, "Losses.")
    else:
        print("You have", Wins, "Wins and", Losses, "Losses.")

player = False

while player == False:
    r = randint(0,2)
    # print("rand", r)
    computer = choices[r]
    player = input("Rock, Paper, or Scissors? ")
    print("The computer chose",computer, "and you chose", player)
    if player == computer:
        print("Tie!")
        counter_func()
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "wraps", player) 
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", player, "crushes", computer)
            Wins = Wins + 1
            counter_func() 
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            Losses = Losses + 1
            counter_func()  
        else: 
            print("You win!", player, "wraps", computer)
            Wins = Wins + 1
            counter_func()   
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
            Losses = Losses + 1
            counter_func()  
        else:
            print("You win!", player, "cuts", computer)
            Wins = Wins + 1
            print(counter_func())   
    else:
        print("That's not a valid move. Check your spelling.")
    player = False
    computer = choices[r]
      
    
        


        
        





   
