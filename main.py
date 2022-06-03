from random import randint

#create a list of play options
t = ["R", "P", "S"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Enter your choice: R, P, S?")
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "P":
        if computer == "S":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "S":
        if computer == "R":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("error")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
