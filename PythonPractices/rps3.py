import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("")
    playerchoice = input("Please Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1, 2 or 3")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    # print("")
    # print("You choose " + playerchoice + ".")
    # print("Computer Choose " + computerchoice + ".")
    # print("")

    # or

    print("")
    print("You choose " + str(RPS(player)).replace('RPS.', "") + ".")
    print("Computer Choose " + str(RPS(computer)).replace('RPS.', "") + ".")
    print("")

    if player == 1 and computer == 3:
        print("🎉 you win!")
    elif player == 2 and computer == 1:
        print("🎉 you win!")
    elif player == 3 and computer == 2:
        print("🎉 you win!")
    elif player == computer:
        print("😳 Tie game!")
    else:
        print("🐍 Computer wins!")

    print("\nPlay again?")

    while True:       
        playagain = input("\nY for yes or \nQ for Quit\n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye 👋")


play_rps()