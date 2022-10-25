# Hangman Game Animal Edition

## UX

### User Demographic

This Python Terminal Game is meant for:

 - Anyone who has the possiblity to run the program to decompress playing a hangman game that only features words from the animal kingdom.

### User Stories

#### As a player I expect
- To see a hangman picture progress as I submit a wrong guess
- To see the amount of letters the word contains and the correct place(s) of the correctly guessed letters in the word.
- To get some feedback when i win/lose
- To see what the word is that I did not manage to guess.

### User Goals

 - Complete the hidden word before the hangman picutre is completed.

### Requirements

A python terminal program that is made completely with python and contains various advanced functionalities.

### Design

For design, since it is a program running in the terminal, the only design elements would be the hangman itself and the win and loss "graphics" and the latter two was made by me and the first one along with the words used are from the [hangmanworbank by chrishorton on github](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)

The aim is to make sure that the player is able to easily follow along the various prints to the console and that means that I slowed down some of the lines to ensure a more enjoyable experience.

## Features 

### Menu

![menu](/readme-imgs/menu.png)

As the picture depicts, the items in the main menu are as follows:
 - Play
 - Instructions
 - Quit
The program validates if the players input is indeed 1 number, it returns an error message if it is not, and if it is above 3, it lets the player know that the menu is only between 1-3

![menuval](/readme-imgs/menval.png)
![menuScopeError](/readme-imgs/menscope.png)

Below are the detailed walkthroughs and pictures of each menu item.

### Play

#### Initial window
![play1](/readme-imgs/play1.png)
- Prints the initial hangman board
- Asks the player for a letter
- Validates the letter and checks if it is correct
- Feedback if wrong or right
- Hangman and list of wrong guesses keeps progressing as game goes on, see images below
- Loss screen and victory screen is essentially the same, with the text and gamestate being different, images below.

Validator caught an invalid character:

![val](/readme-imgs/val.png)

Right guess:

![right](/readme-imgs/right.png)

Wrong guess:

![wrong](/readme-imgs/wrong.png)

Gamestate progression:

![gamestate](/readme-imgs/play2.png)

Loss:

![loss](/readme-imgs/loss.png)

Win difference from lost:

![win](/readme-imgs/win.png)

Ingame quit:

![win](/readme-imgs/igquit.png)

### Instructions

- Prints out the instructions of the program and the rules of hangman.
- Waits for the player to press enter before it returns to the main menu.

![instructions](/readme-imgs/instructions.png)

### Quit
![quitscr](/readme-imgs/quit.png)

- Asks the player to confirm by writing "q" before quitting to ensure it is not done by mistake

### In general for all pages
All pages contain some delays in the code to make the transitions between the pages less jarring, as the instant nature of the terminal can be a bit confusing, so adding these small text of "doing ..." and such with a delay I found was a positive change.


### Features Left to Implement

- Continiuos mode: keep guessing new words untill the lives run out.
- Theme picker: not just animals, but books, movies, cars, games to name a few.

## Technologies used

- [Python](https://www.python.org/)

## Testing 

### Tests Executed
Test exectued to ensure that the program is running as is intended.

 - Ensuring that the input validators accurately validates the inputs in the different parts of the program
 - Test that all the different menu items / input prompts behave as expected.

Listed is the main issues discovered.

1. Whenever the game was prompted to start the menu kept showing up
 - Solution: corrected the while loops logic statement so that it would be true from the beginning, as it was set to fales.
2. The player was allowed to input a value greater than the menu items
 - Solution: added an else to accompany the if and elif statements in the menu code.
3. The player could guess the same letter over and over again
 - Solution: I converted all the inputs to upper with the function .upper(), as it also hinders issues with upper/lower case not counting as the same character.

### Validator Testing 

### Unfixed Bugs

All known bugs have been squashed

## Development and Deployment

The development of this code was done exclusively in GitPod, with the changes being tracked and pushed on GitHub. The initial template of the project was made by the Code Institute

The live version of the project is deployed on Heroku for the time being following the steps outlined by the Code Institute


## Content 

- The Hangman Wordbank and hangman text graphics used in this project was made by chrishorton and can be found [here](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)
- The Clear function was found on [stackoverflow](https://stackoverflow.com/a/684344)