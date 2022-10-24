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
    # Loop for the menu
    while running is True:
        # Prints the menu
        print('\nWelcome to Animal Themed Hangman!\n'
              'Where all words are animals!\n')
        print('1. Play\n')
        print('2. Instructions\n')
        print('3. Quit\n')
        user_input = input('Navigate the menu by typing '
                           'the corresponding number:\n')
        if input_validation(user_input, 'number') is True:
            if user_input == '1':
                # Game launch with a transition
                print('\nPreparing gameboard...\n')
                time.sleep(1)
                print('\nTo quit to menu, type "quit"\n')
                game_running()
            elif user_input == '2':
                # Show instructions with a transition
                print('\nFinding Instructions Sheet...\n')
                time.sleep(1)
                instructions()
            elif user_input == '3':
                # Quit game menu option, has to be confirmed, to avoid
                # accidental quitting.
                user_input = input('To confirm you want to quit the game\n'
                                   'Type "q", type anything else to return \n')
                if user_input.upper() == 'Q':
                    print('Quitting...')
                    time.sleep(1)
                    print('Quit successfully')
                    exit()
                print('Reurning to menu..')
                time.sleep(1)
            else:  # Prints message if the input is not assigned to a menu item
                print('\nMenu is between 1-3, there are hidden menu items!\n')
                time.sleep(1)


def game_start():
    """
    Generates the word to be guessed and prints the initial gameboard.
    """
    # stores the words values of the wordbank module
    # and randomly picks one with the random module.
    words = hangmanwordbank.words
    word = random.choice(words).upper()

    print(hangmanwordbank.HANGMANPICS[0])
    print('=================')
    print('Progress:')
    print(len(word)*'_ ')
    print('=================')
    print("Wrong Guesses:")
    print("None")
    print('=================')
    # returns the randomised word
    # to the game_running function
    return word


def game_running():
    """
    Function that is running as long as the game is running,
    Stores all the guesses and sets the word to be guessed and
    keeps track of the amount of wrong guesses needed for
    the game to end and calls the end function.
    """
    # calls game_start function to pick the word to be guessed.
    # Creates a list for previous guesses and total wrong guesses
    word_to_be_guessed = game_start()
    guessed = []
    tot_wrong = 0

    # Loop to keep going as long as the man hasn't been fully hung.
    while tot_wrong < len(hangmanwordbank.HANGMANPICS)-1:
        # Prompts the players guess
        usr_guess = input('Guess a letter:\n').upper()
        # If true and confirmed, returns to main menu
        if usr_guess == 'QUIT':
            user_input = input('To confirm you want to quit the game\n'
                               'Type "q", type anything else to return \n')
            if user_input.upper() == 'Q':
                print('Quitting...')
                time.sleep(1)
                print('Quit successfully')
                game_menu()
            print('Reurning to game..')
            time.sleep(1)
        if input_validation(usr_guess, 'letter'):  # Checks if input is valid

            if usr_guess not in guessed:  # Checks if guess is duplicate
                guessed.append(usr_guess)  # Store guess in the list
                if usr_guess in word_to_be_guessed:  # Prints success
                    print(f"The letter {usr_guess} is in the word")
                    time.sleep(1)
                else:  # Prints fail + logs it
                    tot_wrong += 1
                    print(f"The letter '{usr_guess}' is not in the word")
                    time.sleep(1)
                # Sends info to update the gameboard
                game_board_update(guessed, tot_wrong, word_to_be_guessed)
            else:  # Lets player know they guessed a duplicate.
                print(f"You already guessed'{usr_guess}', try again")
                time.sleep(1)
    game_loss(word_to_be_guessed)  # Calls the loss function.


def input_validation(usr_input, char_type):
    """
    Validates the users input.
    """
    try:
        # Checks if the input is more than 1 character
        if len(usr_input) > 1:
            raise ValueError(  # Error message for too many chars
                "Too many characters in your input, it contains "
                f"{len(usr_input)} characters instead of one"
            )
        # If statements depending on value of the passed through char_type
        if char_type == 'number':  # Checks if int
            int(usr_input)

        if char_type == 'letter':  # Checks if letter
            if usr_input.isalpha() is not True:
                raise ValueError(  # Error message for wrong type
                    "Only letters accepted as valid guesses!"
                )
    except ValueError as e:  # Prints out the error message
        print(f"Invalid input: {e}\n")
        time.sleep(1)
        return False

    return True  # Returns true if no error is found


def game_board_update(guessed, tot_wrong, word):
    """
    Updates the hangman gameboard.
    """
    # Prints hangman iteration based on the total wrong guesses
    graphic = hangmanwordbank.HANGMANPICS[tot_wrong]
    # strings for word and wrong guesses to be printed in the gameboard
    word_progress = ""
    wrong_guess = ""
    for i in word:  # Loop for word progress
        if i in guessed:
            word_progress = word_progress + f"{i} "
        else:
            word_progress = word_progress + "_ "
    for y in guessed:  # Loop for wrong guesses
        if y not in word:
            wrong_guess += f"{y} "
    # New gameboard print
    print(graphic)
    print('=================')
    print('Progress:')
    print(word_progress)
    print('=================')
    print("Wrong Guesses:")
    print(wrong_guess)
    print('=================')

    # Checks to see if all the letters has been guessed
    # Calls win function if it does.
    if "_" not in word_progress:
        game_win()


def game_win():
    """
    Displays the victory message.
    """
    # Printing the win message
    print('#################')
    print('#    Congrats!  #')
    print('#################')
    time.sleep(.5)
    print("You won the game!")
    time.sleep(.5)
    input('Press enter to return to the menu')
    print('Returning to menu...')
    time.sleep(1)
    game_menu()  # Return to menu


def game_loss(word):
    """
    Displays the loss message.
    """
    # Prints loss message
    print('#################')
    print('#    You Lost   #')
    print('#################')
    time.sleep(.5)
    print("You let him hang")
    time.sleep(.5)
    print(f"The answer was '{word.upper()}'\nWas it really that hard?\n")
    time.sleep(.5)
    input('Press enter to return to the menu')
    print('Returning to menu...')
    time.sleep(1)
    game_menu()  # Return to menu


def instructions():
    """
    Displays the Instructions for the game.
    """
    # Rules print
    print('''
    Animal Hangman Rules:
    - Guess the word that is hidden
    - All words are different animals.
    - W rong guesses gets displayed below
    - Right guesses are displayed in the right position in the word.
    - If the man gets hung before you complete the word, you lose.
    - If you guess the word before he gets hung you win.

    Input:
    - Input number corresponding to menu items, error message if not
      a appropriate value.
    - Input letter for guesses, not case sensetive, checks if letter
      is a leter and if it is unique.
    - type quit while playing to quit to main menu

    ''')
    input('Press enter to return to the menu.')
    print('Returning to menu...')
    time.sleep(1)
    game_menu()  # Return to menu


game_menu()  # Calls function to run game
