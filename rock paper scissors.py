from random import randint

choices = ["Rock", "Paper", "Scissors"]
Wins = 0
Losses = 0 

player = False

while player == False:
    r = randint(0,2)
    # print("rand", r)
    computer = choices[r]
    player = input("Rock, Paper, or Scissors? ")
    print("The computer chose",computer, "and you chose", player)
    if player == computer:
        print("Tie!")
        if Wins == 1 or Losses == 1:
            print("You have", Wins, "Win and", Losses, "Loss.")
        else:
            print("You have", Wins, "Wins and", Losses, "Losses.")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "wraps", player) 
            Losses = Losses + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.")  
        else:
            print("You win!", player, "crushes", computer)
            Wins= Wins + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.") 
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            Losses= Losses + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.") 
        else: 
            print("You win!", player, "wraps", computer)
            Wins= Wins + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.")  
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
            Losses= Losses + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.") 
        else:
            print("You win!", player, "cuts", computer)
            Wins= Wins + 1
            if Wins == 1 or Losses == 1:
                print("You have", Wins, "Win and", Losses, "Loss.")
            else:
                print("You have", Wins, "Wins and", Losses, "Losses.")   
    else:
        print("That's not a valid move. Check your spelling.")
        break

    player = False


        
        





   
