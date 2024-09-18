# Idea project by geeksforgeeks.org
import random
from unittest.result import failfast


def wordGuessingGameSystem():
    attemptCounter = 0
    flag = False
    charGuess = ""
    wordList = ["BLUE"]
    # random_words = [
    #     "APPLE",
    #     "BANANA",
    #     "CAT",
    #     "DOG",
    #     "ELEPHANT",
    #     "FISH",
    #     "GRAPE",
    #     "HOUSE",
    #     "ICE",
    #     "JUNGLE",
    #     "KITE",
    #     "LION",
    #     "MOON",
    #     "NIGHT",
    #     "ORANGE",
    #     "PEN",
    #     "QUEEN",
    #     "ROSE",
    #     "SUN",
    #     "TREE",
    #     "UMBRELLA",
    #     "VIOLIN",
    #     "WATER",
    #     "XYLOPHONE",
    #     "YELLOW",
    #     "ZEBRA",
    #     "ANT",
    #     "BOAT",
    #     "CAR",
    #     "DESK",
    #     "EGG",
    #     "FAN",
    #     "GOAT",
    #     "HAT",
    #     "INK",
    #     "JACKET",
    #     "KEY",
    #     "LAMP",
    #     "MOUSE",
    #     "NOTEBOOK",
    #     "OCEAN",
    #     "PIZZA",
    #     "QUIET",
    #     "RABBIT",
    #     "STAR",
    #     "TRAIN",
    #     "UMBRELLA",
    #     "VASE",
    #     "WHALE",
    #     "YOGURT",
    #     "ZOO",
    # ]
    print("\n=== Welcome to Word Guessing Game! ===")
    userName = input("Hey What is your name: ")
    print(f"Hei {userName} and Good Luck!")
    randomWord = random.choice(wordList)
    # lenRandomWord = len(randomWord)
    while attemptCounter < 13:
        failedChars = 0
        for chars in randomWord:
            if chars not in charGuess:
                failedChars += 1
        if failedChars == 0:
            flag = True
            break
        attemptCounter += 1
        print(f"\n--- Attempts {attemptCounter} ---")
        for chars in randomWord:
            if chars in charGuess:
                print(chars, end="")
            else:
                print("_", end="")
        while True:
            guess = input("\nGuess the word: ").upper()
            print(f"{len(guess)} {len(randomWord)}")
            if len(guess) <= len(randomWord):
                for chars in guess:
                    if chars not in charGuess:
                        charGuess += chars
                break
            else:
                print(
                    "Please make sure the length of the characters you enter is less than or equal to the length of the word being guessed."
                )
    if flag == True:
        if attemptCounter == 1:
            print(
                f'\nCONGRATULATIONS! You have guessed the word "{randomWord}" in {attemptCounter} attempt.'
            )
        else:
            print(
                f'\nCONGRATULATIONS! You have guessed the word "{randomWord}" in {attemptCounter} attempts.'
            )
    else:
        print(f"\nYou Lose!\nThe word is {randomWord}\nBetter luck next time!")


def main():
    while True:
        print("\n=== Welcome to my Third Project ===")
        menuChoosing = input(
            "Menu:\n1. Play Word Guessing Game\n2. Quit Program\nSelect Menu (Number): "
        )
        match menuChoosing:
            case "1":
                wordGuessingGameSystem()
            case "2":
                break
            case _:
                print("Please Select Menu Number!!!\n")


if __name__ == "__main__":
    main()
