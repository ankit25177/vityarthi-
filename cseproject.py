import random

def number_guessing_game():
    """
    A simple number guessing game.
    The computer picks a random number, and the user tries to guess it.
    """
    # 1. Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # 2. Generate the secret number
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Initialize game variables
    guesses_taken = 0
    guess = 0
    
    print(" Welcome to the Number Guessing Game! ")
    print(f"I am thinking of a number between {lower_bound} and {upper_bound}.")
    print("Try to guess it!")
    
    # 3. Game loop
    while guess != secret_number:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            guesses_taken += 1
            
            # 4. Provide feedback
            if guess < lower_bound or guess > upper_bound:
                print(f"🚨 Your guess is outside the range ({lower_bound}-{upper_bound}). Try again.")
            elif guess < secret_number:
                print("Too low! ⬇ Guess higher.")
            elif guess > secret_number:
                print("Too high! ⬆ Guess lower.")
            
        except ValueError:
            print("🛑 Invalid input. Please enter a whole number.")

    # 5. Winning message (This executes when the loop condition guess != secret_number is false)
    print("\n CONGRATULATIONS! You complete it! 🎉")
    print(f"The number was *{secret_number}*.")
    print(f"You took *{guesses_taken}* guesses.")

# Start the game
# number_guessing_game()
