import random
def number_guessing_game ():
    print("🎯 Welcome to the Number Guessing Game!")
    play_again = "yes"

    while play_again.lower() in ["yes", "y"]:
        secrect_number = random.randint(1, 10)
        attempts = 0
        guessed_correctly = False

        print("\nI'm thinking of a number between 1 and 10")

        while not guessed_correctly:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                attempts += 1

                match guess:
                    case _ if guess == secrect_number:
                        print(f"🎉 Congractulations you guessed the number in {attempts} attempts .\n")
                        guessed_correctly = True 
                    case _ if guess > secrect_number:
                        print("📈 Oops, your guess is a bit high. Try again!")
                    case _ if guess < secrect_number:
                        print("📉 Nope, your guess is a bit low. Give it another shot")
            except ValueError:
                print("Invalid input! Please enter a valid number")

        play_again = input("Do you want to play again? (yes/no): ")

    print("👋 Thanks for playing! Goodbye")

#Start the game
number_guessing_game()






