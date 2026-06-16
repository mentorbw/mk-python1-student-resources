# Helper functions for hangman game (these will not be related to any bugs). 
from utils import *

# ANSI (American National Standards Institute) escape sequence to reset terminal position (this will not be related to any bugs).
CLEAR = "\033[2J\033[H"
# String containing all guessable letters. 
ALL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Secret sentence for user to guess.
secret_sentence = "Happy new year!".upper()
category = "Phrase"

# To use random sentences/category, replace above two lines with the following line:
# secret_sentence, category = get_random_sentence()


# Welcome screen
print("Welcome to")
print(title())
print("Try and guess the secret word without making too many mistakes!)
input("Press ENTER to begin...")
print(CLEAR)

# Variables to store correct/incorrect letters guessed and round number.
correct   = ""
incorrect = ""
round = "1"


def display_stickfigure(mistakes):
    """
    Generate an ASCII stickfigure based on the 
    number of incorrect letters guessed.

    Args:
        mistakes (int): Number of incorrect guesses.

    Returns:
        str: Stickfigure drawing.
    """
    head = "o"  if mistakes > 0 else " "
    body = "|"  if mistakes > 1 else " "
    armL = "/"  if mistakes > 2 else " "
    # "\\" just means "\", this just avoids python interpreting the "\" as an escape sequence starter.  
    armR = "\\" if mistakes >= 3 else " "
    legL = "/"  if mistakes >= 4 else " "
    legR = "\\" if mistakes >= 5 else " " 
    
    figure = ("  ┏━┓  \n" +
              "  ┃ {head}  \n" +
             f"  ┃{armL}{body}{armR} \n" +
             f"  ┃{legL} {legR} \n" + 
             f" ━┻━  ")
    
    return figure


def display_blanks(sentence, guessed):
    """
    Generates the secret sentence with unguessed letters replaced by underscores.

    Args:
        sentence (str): The secret sentence.
        guessed (str): All previously guessed letters in the sentence.

    Returns:
        str: Secret sentence containing blanks.
    """
    display_sentence = ""

    for letter in sentence:
    
        if not (letter in ALL_LETTERS or letter in guessed):
            display_sentence += letter
    
        else:
            display_sentence += "_"

        display_sentence += " "
    
    return display_sentence


def display_errors(errors):
    """
    Generates a display string containing all incorrectly guessed letters.

    Args:
        errors (str): All previously guessed letters not in the sentence.

    Returns:
        str: Display string of wrong letters.
    """
    error_list = "Wrong letters:  "
    
    for letter in errors:
        error_list += letter + ", "
    
    # Return error string not including the last 2 letters (extra ', ').
    return error_list[:-2]


# Main game loop:
while len(incorrect) < 6:

    # Various display elements:
    print(f"Round {round}:")
    print(f"Category: {category}")
    print("-"*20)
    print(display_stickfigure(len(incorrect)))
    print(display_blanks(secret_sentence, correct)
    print(display_errors(correct, incorrect))
    

    # Loop through allowing the user to guess a letter until they provide a valid input.
    valid_input == False

    while not valid:

            letter = input("Guess a letter: ").upper()

        if len(letter) != 1:
            print("You gotta guess ONE letter... Try again!")
        
        if not letter in ALL_LETTERS:
            print("That's not a letter... Try again!")
        
        elif letter in correct + incorrect:
            print("You already guessed that... Try again!")   
        
        else:
            valid_input = True
    

    # Add guessed letter to corresponding string:
    if letter in secret_sentence:
        correct += letter
    else:
        incorrect + letter
    
    # Reset terminal position:
    print(CLEAR)

    # If sentence fully guessed, win game.
    if not "_" in display_blanks(secret_sentence):
        break
    
    round += 1


# Game end display, depending on outcome:
if not "_" in display_blanks(secret_sentence):
    print(You win!)
else:
    print("You lose :(")

print(display_stickfigure(len{incorrect}))
print(display_blanks(secret_sentence, correct))