# vityarthi-
## 🎮 Number Guessing Game

This is a simple, command-line Python game where the user tries to guess a randomly generated secret number within a set range and a limited number of attempts.

-----

## 🚀 Getting Started

### Prerequisites

You only need **Python 3** installed on your system.

### How to Run

1.  **Save the code:** Save the provided Python code into a file named `guessing_game.py`.

2.  **Open your terminal/command prompt.**

3.  **Navigate to the directory** where you saved the file.

4.  **Execute the script** using the Python interpreter:

    ```bash
    python guessing_game.py
    ```

-----

## 🕹️ How to Play

### Game Objective

The computer selects a random integer between **1 and 100**. Your goal is to guess this number in **7 attempts or less**.

### Gameplay

1.  The game will start and tell you the range and the number of attempts you have.
2.  Enter your integer guess when prompted.
3.  The game will provide **feedback** after each guess:
      * **"Too low\! ⬇ Guess higher."**
      * **"Too high\! ⬆ Guess lower."**
      * The prompt will also show the **narrowed range** (e.g., `(25-75)`) to help you zero in on the secret number.
4.  If you guess correctly, you win\!
5.  If you run out of attempts, you lose, and the secret number is revealed.
6.  You will be asked if you want to play again after each round.

-----

## ⚙️ Game Configuration

You can easily modify the game's difficulty by changing the variables at the beginning of the `number_guessing_game()` function:

| Variable | Description | Default Value |
| :--- | :--- | :--- |
| `lower_bound` | The starting number of the guessing range. | `1` |
| `upper_bound` | The ending number of the guessing range. | `100` |
| `max_guesses` | The maximum number of attempts the user has. | `7` |

> 📝 **Tip:** The optimal number of guesses for a range of $N$ numbers is approximately $\log_2(N)$. For the default range (100), $\log_2(100) \approx 6.64$, making 7 guesses a fair and challenging limit.

-----

## 🔧 Code Structure

The game relies on Python's built-in `random` module for generating the secret number and includes robust features:

  * **Error Handling:** Uses a `try...except ValueError` block to ensure the user inputs a valid integer. Non-numeric input does not count as a guess.
  * **Attempt Tracking:** Keeps a count of `guesses_taken` and enforces the `max_guesses` limit.
  * **Replay Functionality:** An outer `while True` loop allows the user to play continuously until they choose to exit.

Would you like the original Python code block included directly in this README?
