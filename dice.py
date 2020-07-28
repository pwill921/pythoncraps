import random as r
import sys

# Function that asks the user if they want to play again
def play_agian():
    play = input("Would you like to roll again? y/n ")
    if play == "y" or play == "Y":
        comeout()
    elif play == "n" or play == "N":
        sys.exit()
    else:
        comeout()

#function for come out phase
def comeout():
    # tells user we are in the come out phase and to press enter to roll dice
    print("The Come Out Phase!")
    input("Press ENTER to roll dice!")

    # creating variable for the dice rolled during the comout phase
    dice_total = r.randint(1, 6) + r.randint(1, 6)

    # if statement that tells the system what dice total will win, lose, or take us to the next phase
    # if 7 or 11 is rolled then the user wins
    if dice_total == 7 or dice_total == 11:
        print(f"You rolled a {dice_total}! Winner!")
        play_agian()
    # if a 2 3 or 12 is rolled then the user loses
    elif dice_total == 2 or dice_total == 3 or dice_total == 12:
        print(f"You rolled a {dice_total}")
        print("Craps! You lose!")
        play_agian()
    # if anything else is rolled then we go into the point phase which is defined in the next function
    else:
        print(f"You rolled a {dice_total}")
        print(f"The point is {dice_total}")
        print(f"You need to roll a {dice_total} before you roll a 7 to win!")
        point_phase(dice_total)

# function for point phase
def point_phase(dice_total):
    # asks user to roll dice
    input("Press Enter to roll dice!")

    # variable for dice total during point phase. not to be confused with dice_total which is during comeout phase
    dice_totalPoint = r.randint(1, 6) + r.randint(1, 6)

    # if statement that compares our dice_totalPoint with the original dice total
    if dice_totalPoint == dice_total:
        print(f"{dice_totalPoint}!!!!!! You win!!!!")
        play_agian()
    elif dice_totalPoint == 7:
        print(f"{dice_totalPoint}! You Lose!")
        play_agian()
    else:
        print(f"You rolled a {dice_totalPoint}! Roll again!")
        roll_again(dice_total)

# Function to roll the dice again after point has been established
def roll_again(dice_total):
    # asks user to press enter to roll dice
    input("Press Enter to roll dice!")

    # same as point phase but we use this when point or 7 isn't rolled
    dice_totalPoint = r.randint(1, 6) + r.randint(1, 6)

    if dice_totalPoint == dice_total:
        print(f"You rolled a {dice_totalPoint}! You Win!")
        play_agian()
    elif dice_totalPoint == 7:
        print(f"{dice_totalPoint}! You Lose!")
        play_agian()
    else:
        print(f"You rolled a {dice_totalPoint}! Roll again!")
        roll_again(dice_total)




def main():
    print("Welcome to Python Craps!")
    input("Press Enter to play!")
    comeout()
    point_phase()
    roll_again()




if __name__=="__main__":
    main()