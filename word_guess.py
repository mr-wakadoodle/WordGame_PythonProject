"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with
BORDER = '*'


def play_game(secret_word, initial_word_hint):
    guesses = INITIAL_GUESSES
    initial_word = initial_word_hint
    while initial_word != secret_word and guesses > 0:
        follow_back = True
        print("The word now looks like this: " + initial_word)
        print("You have " + str(guesses) + " guesses left")
        ch = input("Type a single letter here, then press enter: ").upper()
        while follow_back:
            if len(ch) > 1:
                print("Guess should only be a single character.")
                print("The word now looks like this: " + initial_word)
                print("You have " + str(guesses) + " guesses left")
                ch = input("Type a single letter here, then press enter: ").upper()
            else:
                follow_back = False
        result = check_letter(ch, secret_word)
        if result:
            print("That guess is correct.")
            for index in range(len(secret_word)):
                if ch == secret_word[index]:
                    initial_word = initial_word[:index] + ch + initial_word[index + 1:]
        else:
            print("There are no " + ch + "'s in the word")
            guesses = guesses - 1

    if initial_word == secret_word:
        print("Congratulations, the word is: " + initial_word)
    else:
        print("Sorry, you lost. The secret word was: " + secret_word)


def check_letter(ch, word):
    if ch in word:
        return True
    return False


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    """"print(game_word)
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER' """
    opened_file = open(LEXICON_FILE)
    word_list = []
    for line in opened_file:
        word = line.strip()
        word_list.append(word)

    game_word = random.choice(word_list)
    return game_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """

    print(
        "The WordGuess game::\nWhen the user plays WordGuess, the computer first selects a secret word at random from"
        "\na list built into the program. The program then prints out a row of dashes—one for each\n"
        "letter in the secret word and asks the user to guess a letter. If the user guesses a letter that\n"
        "is in the word, the word is redisplayed with all instances of that letter shown in the correct\n"
        "positions, along with any letters correctly guessed on previous turns. If the letter does not\n"
        "appear in the word, the user is charged with an incorrect guess. The user keeps guessing\n"
        "letters until either (1) the user has correctly guessed all the letters in the word or (2) the\n"
        "user has made eight incorrect guesses. ")
    hint_word = ""
    print("\nCode is changed a bit and few hints are added depending on the difficulty level")
    secret_word = get_word()
    secret_word.upper()
    word_length = len(secret_word)
    initial_word = '-' * word_length
    while True:
        print("1. Easy\n2. Medium")
        level = int(input("Select the difficulty level: "))
        # Adding hints based on the difficulty level
        if level == 1:
            a = random.randint(0, len(secret_word) - 1)
            b = random.randint(0, len(secret_word) - 1)
            while b == a:  # This is done so that no same random index is generated
                b = random.randint(0, len(secret_word) - 1)

            initial_word = initial_word[:a] + secret_word[a] + initial_word[a + 1:]
            initial_word = initial_word[:b] + secret_word[b] + initial_word[b + 1:]
            break

        elif level == 2:
            a = random.randint(0, len(secret_word) - 1)
            initial_word = initial_word[:a] + secret_word[a] + initial_word[a + 1:]
            break

        else:
            print("Wrong Input")

    print("")
    print("Note: Already filled characters may or may not have more occurrences! \n\n")
    play_game(secret_word, initial_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
