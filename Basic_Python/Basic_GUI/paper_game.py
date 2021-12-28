import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = 0
    while player not in choices:
        player = input("Rock/ paper/ scissors: ").lower()
    if computer == player:
        print("Tie!")
    elif computer == "rock":
        if player == "paper":
            print(computer)
            print(player)
            print("You win!")
        elif player == "scissors":
            print(computer)
            print(player)
            print("You lose!")
    elif computer == "paper":
        if player == "rock":
            print(computer)
            print(player)
            print("You lose!")
        elif player == "scissors":
            print(computer)
            print(player)
            print("You win!")
    elif computer == "scissors":
        if player == "paper":
            print(computer)
            print(player)
            print("You lose!")
        elif player == "rock":
            print(computer)
            print(player)
            print("You win!")

    a = input(print("Play gain? Yes/No")).lower()
    if(a != "yes"):
        break
print("Se ya!")