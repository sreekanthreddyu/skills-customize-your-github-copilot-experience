
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game using Python. You will practice string manipulation, loops, conditionals, and random selection while creating an interactive game.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the core game setup by defining a word list and writing logic to randomly select a word for each round.

#### Requirements
Completed program should:

- Define a predefined list of words for the game to choose from
- Randomly select one word at the start of each game using the `random` module
- Display the hidden word as underscores in `_ _ _` format, one per letter

### 🛠️ Implement the Game Loop

#### Description
Write the main game loop that accepts player guesses, updates the displayed word, and tracks remaining attempts.

#### Requirements
Completed program should:

- Prompt the player to guess a letter each turn
- Reveal correctly guessed letters in their proper position(s)
- Track and display the number of incorrect guesses remaining
- Keep track of previously guessed letters and notify the player of duplicates

### 🛠️ Handle Win and Lose Conditions

#### Description
Add logic to detect when the game is over and display an appropriate message to the player.

#### Requirements
Completed program should:

- End the game and display a win message when the full word is guessed
- End the game and display a lose message when all attempts are exhausted
- Show the correct word to the player when the game ends
