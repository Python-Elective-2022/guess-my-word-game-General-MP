import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    '''
    for every letter in secret_word
      if letter not in letter_guessed
        add letter in lowercase to letter_missing
      else
        pass
    return whether the list of word missing is empty
    '''
    letter_missing = [letter.lower() for letter in secret_word if letter not in letters_guessed]
    return len(letter_missing) == 0


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    '''
    for every letter in secret_word
      if letter in letter_guessed
        add letter to display
      else
        add "_" to display
    return display joined into string
    '''
    display = [letter.lower() if letter in letters_guessed else "_ " for letter in secret_word]
    return "".join(display)
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    '''
    for every letter in list of a - z
      if letter not in letter_guessed
        add letter to not_guessed
      else
        pass
    '''
    not_guessed = [letter for letter in string.ascii_lowercase if letter not in letters_guessed]
    return "".join(not_guessed)


def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    '''
    output "Let the game begin!"
    set number of letter to word's length
    output "I am thinking of a word with {number of letter} letters."
    set maximum guess number to 8
    create empty list 

    while number of time guess not exceed 8 and word had not been guess
      get letter that had not been guessed
      output "You have {number of guess} guesses remaining."
      output "Letters available to you: {letter that had not been guessed}"
      prompt for a letter and convert to lowercase
      if letter is in secret_word
        add letter to guess list
        reduce number of guess by 1
        if letter guessed is correct
          output "Correct: " + _ _ _ _ _ with position of letter guessed replaced with letter
        else
          output "Correct: " + _ _ _ _ _
      else letter already been guessed
        output "You fool! You tried this letter already: _ _ _ _ _"
      if word guessed
        output "You WIN"
      else number of guess ran out
        output "GAME OVER !The word was {secret_word}."

    '''
    print("Let the game begin!")
    letters_number = len(secret_word)
    print(f"I am thinking of a word with {letters_number} letters.")
    guess_number = 8
    guess_list = []
    while guess_number != 0 and not is_word_guessed(secret_word, guess_list):
      guessed_letter = get_available_letters(guess_list)
      print(f"\nYou have {guess_number} guesses remaining.")
      print(f"Letters available to you: {guessed_letter}")
      guess = input("Guess a letter: ").lower()
      if guess not in guess_list:
        guess_list.append(guess)
        guess_number -= 1
        if guess in secret_word:
          print("Correct: ", end="")
        else:
          print("Incorrect: ", end="")
        print(f"{get_guessed_word(secret_word, guess_list)}")
      else:
        print(f"You fool! You tried this letter already: {get_guessed_word(secret_word, guess_list)}")
    if is_word_guessed(secret_word, guess_list):
      print("\nYou WIN")
    else:
      print(f"\nGAME OVER !The word was {secret_word}.")


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)


if __name__ == "__main__":
    main()