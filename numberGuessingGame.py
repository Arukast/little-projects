# Idea project by geeksforgeeks.org
import random


def numberGuessingGameSystem():
    print("\n=== Welcome To Number Guessing Game! ===")
    attemptCounter = 0
    while True:
        try:
            lowerLimit, upperLimit = map(
                str,
                input(
                    'Please select range of number do you want to guess (Separated by the symbol " to "), i.e 10 to 100: '
                ).split(" to ", 1),
            )
            lowerLimit, upperLimit = int(lowerLimit), int(upperLimit)
        except ValueError:
            print('Please input two numbers that separated by a " to "\n')
            continue
        if lowerLimit >= 0:
            if upperLimit > lowerLimit:
                print(
                    f"\n--- Let's Play! ---\nThe range you choose is {lowerLimit} to {upperLimit}"
                )
                chosenRandomNumber = random.randint(lowerLimit, upperLimit)
                break
            else:
                print(
                    f"The upper limit cannot be {upperLimit} because the lower limit is greater than or equal to the upper limit!\n"
                )
        else:
            print("The range cannot be negative!\n")
    while True:
        attemptCounter += 1
        userGuess = int(
            input(
                f"\n!!! Attempts {attemptCounter} !!!\nInput your guess(only INTEGER): "
            )
        )
        if userGuess == chosenRandomNumber:
            print(
                f"CONGRATS!!! You have guessed it right, the chosen number is {chosenRandomNumber}, and you guessed it in {attemptCounter} attempts!!!\n"
            )
            break
        elif userGuess > chosenRandomNumber:
            print("Try again! You guessed to high")
        elif userGuess < chosenRandomNumber:
            print("Try again! You guessed to small")


def main():

    while True:
        print("=== Welcome to my second Project ===")
        menuChoosing = input(
            "Menu:\n1. Play Number Guessing Game\n2. Quit Program\nSelect Menu (Number): "
        )
        match menuChoosing:
            case "1":
                numberGuessingGameSystem()
            case "2":
                break
            case _:
                print("Please Select Menu Number!!!\n")


main()
