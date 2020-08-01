from random import randint

choices = ["Rock", "Paper", "Scissors"]
computer = choices[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, or Scissors?")
    print("The AI chose",computer, "and you chose", player)
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "wraps", player)
        else:
            print("You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else: 
            print("You win!", player, "wraps", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        else: 
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid move retard. Check your spelling you idiotic ape.")
    player = False
