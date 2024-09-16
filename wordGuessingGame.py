# Idea project by geeksforgeeks.org
import random


def wordGuessingGameSystem():
    attemptCounter = 0
    flag = False
    charCounter = 0
    charGuess = ""
    wordList = ["blue"]
    # wordList = [
    #     "apple",
    #     "banana",
    #     "cat",
    #     "dog",
    #     "elephant",
    #     "fish",
    #     "grape",
    #     "house",
    #     "ice",
    #     "jungle",
    #     "kite",
    #     "lion",
    #     "moon",
    #     "night",
    #     "orange",
    #     "pen",
    #     "queen",
    #     "rose",
    #     "sun",
    #     "tree",
    #     "umbrella",
    #     "violin",
    #     "water",
    #     "xylophone",
    #     "yellow",
    #     "zebra",
    #     "ant",
    #     "boat",
    #     "car",
    #     "desk",
    #     "egg",
    #     "fan",
    #     "goat",
    #     "hat",
    #     "ink",
    #     "jacket",
    #     "key",
    #     "lamp",
    #     "mouse",
    #     "notebook",
    #     "ocean",
    #     "pizza",
    #     "quiet",
    #     "rabbit",
    #     "star",
    #     "train",
    #     "umbrella",
    #     "vase",
    #     "whale",
    #     "yogurt",
    #     "zoo",
    #     "blue",
    # ]
    print("\n=== Welcome to Word Guessing Game! ===")
    userName = input("Hey What is your name: ")
    print(f"Hei {userName} and Good Luck!")
    randomWord = random.choice(wordList)
    while attemptCounter < 13:
        attemptCounter += 1
        print(f"\n--- Attempts {attemptCounter} ---")
        for char in randomWord:
            if char in charGuess:
                charCounter -= 1
                print(char, end="")
            else:
                print("_", end="")
                charCounter += 1
        if charCounter == 0:
            flag = True
            break
        else:
            for char in input("\nGuess the word: "):
                charGuess += char
    if flag == True:
        print(
            f'CONGRATULATIONS! You have guessed the word "{randomWord}" in {attemptCounter} attempt(s)!'
        )
    else:
        print(f"\nThe word is {randomWord}\nBetter luck next time")


def main():
    while True:
        print("=== Welcome to my third Project ===")
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
