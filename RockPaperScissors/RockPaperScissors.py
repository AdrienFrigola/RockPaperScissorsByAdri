import random

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid Input. Try again...")
        continue

    computer_random_nb = random.randint(1, 3)

    computer_move = ""

    if computer_random_nb == 1:
        computer_move = rock
        print(f"The computer chose: {computer_move}")
    elif computer_random_nb == 2:
        computer_move = paper
        print(f"The computer chose: {computer_move}")
    elif computer_random_nb == 3:
        computer_move = scissors
        print(f"The computer chose: {computer_move}")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? [Y]es / [N]o: ")
    if play_again == "Y":
        break
