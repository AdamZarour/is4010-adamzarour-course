import random

def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short Mad Libs-style story using the provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave").
    noun : str
        A noun to use in the story (e.g., "cat", "knight").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "battled").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped through the city while everyone stared in disbelief."
    """
    return f"The {adjective} {noun} {verb} through the city while everyone stared in disbelief."



def guessing_game():
    """
    Plays a number guessing game with the user.

    The function generates a random secret number between 1 and 100 and
    prompts the user to guess until the correct number is found. It prints
    feedback ("Too high!", "Too low!") after each guess and a congratulatory
    message including the number of attempts when the user guesses correctly.

    Notes
    -----
    This function uses ``input()`` and ``print()`` for interaction and returns
    ``None``. It is safe to import the module without starting the game; the
    game only runs when the module is executed as a script.

    Examples
    --------
    Run interactively::

        if __name__ == '__main__':
            guessing_game()
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break



if __name__ == '__main__':
    guessing_game()
