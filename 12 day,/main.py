import random


def game(difficult):
    if difficult == "hard":
        attempts = 5
    elif difficult == "easy":
        attempts = 10
    else:
        print("Error")
        return
    hidden_number = random.randint(1, 100)

    for i in range(1, attempts + 1):
        number = int(input("Make a guess: "))

        if number > hidden_number:
            print(f"Too low\nGuess again\nNumber of attempts: {attempts - i}")
        elif number < hidden_number:
            print(f"Too high\nGuess again\nNumber of attempts: {attempts - i}")
        else:
            if input("You got it right.\nWill you play again? Write 'y' or 'n': ") == "y":
                return True
            else:
                return False


def main():
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking a number between 1 and 100")
    start_game = True
    while start_game:
        difficult = input("Chose difficulty. Type 'easy' or 'hard': ")
        start_game = game(difficult)


if __name__ == '__main__':
    main()
