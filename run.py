import random
import time
import hangmanwordbank

# hangman resources like picture and wordbank from Github
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


def game_menu():
    """
    Function that runs the start menu.
    """
    running = True

    while running is True:
        # Prints the menu

        print('\nWelcome to Animal Hangman!\n ')
        print('1. Play\n')
        print('2. Instructions\n')
        print('3. Quit\n')
        user_input = input('Navigate the menu by typing '
                           'the corresponding number:\n')
        if input_validation(user_input, 'number') is True:
            if user_input == '1':
                game_running()
            elif user_input == '2':
                print('\nintructions\n')
            elif user_input == '3':
                user_input = input('To confirm you want to quit the game\n'
                                   'Type "q"\n')
                if user_input.upper() == 'Q':
                    print('Quitting...')
                    time.sleep(1)
                    print('Quit successfully')
                    exit()
                print('Reurning to main menu..')
                time.sleep(1)
    # checks for user input for the menu items
    # passes validation criteria and input over to input validation
    # if valid then it gets pushed to the right function
    # optional: add difficulty level that can be set.


def game_start():
    """
    Generates the word to be guessed.
    """
    words = hangmanwordbank.words
    word = random.choice(words).upper()

    print(hangmanwordbank.HANGMANPICS[0])
    print('=================')
    print('Progress:')
    print(len(word)*'_ ')
    print('=================')
    print("Previous Guesses:")
    print("None")
    print('=================')
    # returns the randomised word
    # to the game_running function
    return word
    # optional addition: based on letter count (difficulty level)


def game_running():
    """
    Function that is running as long as the game is running,
    Stores all the guesses and sets the word to be guessed and
    keeps track of the amount of wrong guesses needed for
    the game to end.
    """
    word_to_be_guessed = game_start()
    # optional: pass through difficulty setting
    guessed = ""
    tot_wrong = 0
    while tot_wrong < len(hangmanwordbank.HANGMANPICS)-1:
        # Prompts the players guess
        usr_guess = input('Guess a letter:\n').upper()
        if input_validation(usr_guess, 'letter'):
            guessed += f"{usr_guess} "
            if usr_guess in word_to_be_guessed:
                print(f"The letter {usr_guess} is in the word")
            else:
                # logs the wrong answer
                tot_wrong += 1
                print(f"The letter '{usr_guess}' is not in the word")
            # sends info to game board
            game_board_update(guessed, tot_wrong, word_to_be_guessed)
    game_loss(word_to_be_guessed)
    # Checks that the to see if game has been won or lost
    # asks for user input of a letter
    # sends it with criteria to validatiton function
    # if true updates gamestate and pushes info game_board_update
    # loop back
    # if game is won/lost send to won/lost function
    # optional: accepts quit to cancel game session


def input_validation(usr_input, char_type):
    """
    Validates the users input.
    """
 
    try:
        # Checks if the input is more than 1 character
        if len(usr_input) > 1:
            raise ValueError(
                "Too many characters in your input, it contains "
                f"{len(usr_input)} characters instead of one"
            )
        if char_type == 'number':
            int(usr_input)

        if char_type == 'letter':
            if usr_input.isalpha() is not True:
                raise ValueError(
                    "Only letters accepted as valid guesses!"
                )
    except ValueError as e:
        print(f"Invalid input: {e}\n")
        time.sleep(1)
        return False

    return True
    # accepts two inputs, the input to be validated and the expected type
    # if correct send back true + success message
    # if incorrect send back wrong + error message
    # back to game_running


def game_board_update(guessed, tot_wrong, word):
    """
    Updates the hangman gameboard.
    """
    graphic = hangmanwordbank.HANGMANPICS[tot_wrong]
    word_progress = ""
    for i in word:
        if i in guessed:
            word_progress = word_progress + f"{i} "
        else:
            word_progress = word_progress + "_ "

    print(graphic)
    print('=================')
    print('Progress:')
    print(word_progress)
    print('=================')
    print("Previous Guesses:")
    print(guessed)
    print('=================')

    if "_" not in word_progress:
        game_win(tot_wrong)
    # accepts input of wrongs and rights in a list
    # displays the rights in the correct index in the guessed answer
    # displays the wrong in a list next to it
    # draws the hangman dude based on wrong answers
    # return the value to the is running


def game_win(tot_wrong):
    """
    Displays the victory message.
    """
    print('#################')
    print('#    Congrats!  #')
    print('#################')
    time.sleep(.5)
    print("You won the game!")
    time.sleep(.5)
    print(f"With {tot_wrong} \nwrong guessses! ")
    time.sleep(.5)
    print('Returning to menu...')
    time.sleep(1)
    game_menu()


def game_loss(word):
    """
    Displays the loss message.
    """
    print('#################')
    print('#    You Lost   #')
    print('#################')
    time.sleep(.5)
    print("You let him hang")
    time.sleep(.5)
    print(f"The answer was '{word.upper()}'\nWas it really that hard?\n")
    time.sleep(.5)
    print('Returning to menu...')
    time.sleep(1)
    game_menu()


def instructions():
    """
    Displays the Instructions for the game.
    """
    # general rules of hangman
    # amount of wrong answers allowed before the man gets hung
    # what the different menu options do and commands inside the game


game_menu()
