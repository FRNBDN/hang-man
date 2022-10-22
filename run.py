import hangmanwordbank, random

def game_menu():
    """
    Function that runs the start menu.
    """
    running = True

    while running is True:
        print('Welcome to the game of Hangman!')
        print('Navigate the menu by typing the corresponding number!')
        print('1. Play\n')
        print('2. Instructions\n')
        print('3. Quit\n')
        user_input = input()
        if user_input == '1':
            game_running()
        elif user_input == '2':
            print('\nintructions\n')
        elif user_input == '3':
            exit()
        else:
            print('\nNot a valid input\n')
    # checks for user input for the menu items
    # passes validation criteria and input over to input validation
    # if valid then it gets pushed to the right function
    # optional: add difficulty level that can be set.


def game_start():
    """
    Sets up the game, generates the word.
    """
    words = hangmanwordbank.words
    word = random.choice(words)
    return word
    # list of words
    # chooses the word for the game from the list
    # optional: based on letter count (difficulty level)
    # returns the word to the game_running function


def game_running():
    """
    Function that is running as long as the game is running.
    """
    # calls game_start function, optional: pass through difficulty setting
    # Checks that the to see if game has been won or lost
    # asks for user input of a letter
    # sends it with criteria to validatiton function
    # if true updates gamestate and pushes info game_board_update
    # loop back
    # if game is won/lost send to won/lost function
    # optional: accepts quit to cancel game session


def input_validation():
    """
    Validates the users input.
    """
    # accepts two inputs, the input to be validated and the expected type
    # if correct send back true + success message
    # if incorrect send back wrong + error message
    # back to game_running


def game_board_update():
    """
    Updates the hangman gameboard.
    """
    # accepts input of wrongs and rights in a list
    # displays the rights in the correct index in the guessed answer
    # displays the wrong in a list next to it
    # draws the hangman dude based on wrong answers
    # return the value to the is running


def game_win():
    """
    Displays the victory message.
    """
    # shows the general victory screen
    # shows number of right guesses and wrong guesses below


def game_loss():
    """
    Displays the loss message.
    """
    # shows the general loss screen
    # shows number of right guesses and wrong guesses below


def instructions():
    """
    Displays the Instructions for the game.
    """
    # general rules of hangman
    # amount of wrong answers allowed before the man gets hung
    # what the different menu options do and commands inside the game


def main():
    """
    Runs program functions and keeps track of gamestates
    """
    # game_menu()
    game_start()


main()
