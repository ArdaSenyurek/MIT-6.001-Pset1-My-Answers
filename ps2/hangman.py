# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import time

WORDLIST_FILENAME = r"C:\Users\arda_\Downloads\ps2\ps2\words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    wordlist = load_words()
    lstwords = {}
    for words in wordlist:
          if match_with_gaps(my_word, words):
                return lstwords.add(words)


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    counter = 0
    secret_word = str.lower(secret_word)
    for i in letters_guessed:
        letters_guessed[counter] = str.lower(i)
        counter += 1
    #print(letters_guessed)
    return secret_word == ''.join(letters_guessed)

def str_lower(secret_word, letters_guessed):
    
    counter = 0
    secret_word = str.lower(secret_word)
    for i in letters_guessed:
        try:
            letters_guessed[counter] = str.lower(i)
            counter += 1
        except TypeError:
            pass
    # print(letters_guessed)
    # print(secret_word)
    return secret_word

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str_lower(secret_word, letters_guessed)
    temp = []
    counter = 0
    for times in range(len(secret_word)):
        if ' ' == secret_word[times]:
            temp.append(' ')
        else:
            temp.append('_ ')
    for letter in str_lower(secret_word, letters_guessed):
        if letter in letters_guessed:
            temp[counter] = letter
        counter += 1
    # print(temp)
    return ''.join(temp)
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    ascii_low = string.ascii_lowercase
    lst_ascii_low = list(ascii_low)
    for letter in letters_guessed:
        if letter in string.ascii_lowercase:
            try: 
              lst_ascii_low.remove(letter)
            except ValueError:
              pass
    return ''.join(lst_ascii_low)
    


def OpenFile():
      file = open('hints.txt', 'w')
      return file

def writeFile(file, words):
      file.write(words)
      
def CloseFile(file):
      file.close()

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #file = OpenFile() pass to show_possible_matches 
    NumbersRight = 6
    isFirst = True
    didWin = False
    Warnings = 3
    letters_guessed = []
    while NumbersRight >= 0:
      my_word_as_far = get_guessed_word(secret_word, letters_guessed)
      my_word_as_far_no_space = lower_and_remove_white_space(my_word_as_far)
      if isFirst:
        print(secret_word)
        print(f'You have {NumbersRight} left.')
        print(f'Available letters: {get_available_letters(letters_guessed) } ')  
        print(f'I\'m thinking of a word that is {len(secret_word)} letters long.')  
        print(f' Word : {get_guessed_word(secret_word, letters_guessed)} ')
        print(f'Warnings:{Warnings}')
        print('----------------')
        isFirst = False 
      else:
        print(f'You have {NumbersRight} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed) } ')
        print(f'Warnings:{Warnings}')
        letter = input('Please guess a letter:').lower()
        if letter == '*':
          pass
        else:
          letters_guessed.append(letter)
        #print(letters_guessed)
        if letter not in secret_word or letters_guessed.count(letter) != 1 or not letter.isalpha():
          
          if letters_guessed.count(letter) == 1 and letter.isalpha():
            if letter != '*':
              if letter in 'aeiou':
                NumbersRight -= 2
              else:
                NumbersRight -= 1  
              print(f'Oops! That letter is not in my word:{get_guessed_word(secret_word, letters_guessed)}')
              print('----------------')
          
          elif letter == '*':
            counter = 0
            for char in my_word_as_far_no_space:
              if char != '_':
                counter = 1
                break
              else:
                counter = 0      
            if counter == 1:
              print('\nPossible word matches are:')
              print(show_possible_matches(my_word_as_far, letters_guessed))
              print('----------------')
            else:
              print('You need to unreveal 1 letter at least')
              print('----------------')
          
          else:
            if Warnings == 0:
              NumbersRight -= 1 
              print('----------------')
            else:
              Warnings -= 1
              print('----------------')
        else:
          print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)} ')
          print('---------------------')
          
        if is_word_guessed(secret_word, letters_guessed) or letter == secret_word:
          print(f'You had {NumbersRight} guesses left.')
          print(f'Available letters: {get_available_letters(letters_guessed) } ')           
          print('You won haha!')
          didWin = True
          break
    if not didWin:
      print(f'Sorry, you ran out of guesses. The word was \'{secret_word}\'.')
        
      
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def lower_and_remove_white_space(my_word):
  my_word_lower = my_word.lower()
  stripped_lower = my_word_lower.strip()
  list_my_word = list(stripped_lower)
  for char in list_my_word:
    if char == ' ':
          list_my_word.remove(char)
  return ''.join(list_my_word)

def match_with_gaps(my_word, other_word, letters_guessed):
  '''
  my_word: string with _ characters, current guess of secret word
  other_word: string, regular English word
  returns: boolean, True if all the actual letters of my_word match the 
      corresponding letters of other_word, or the letter is the special symbol
      _ , and my_word and other_word are of the same length;
    False otherwise:  
  '''
  Flag = True
  isDone = True
  my_word2 = lower_and_remove_white_space(my_word)
  if len(lower_and_remove_white_space(my_word)) != len(other_word):
    return False
  
  else:
    while Flag and isDone :
      for index in range(len(my_word2)):
        if my_word2[index] != '_' and my_word2[index] != other_word[index]: 
          Flag = False
        if index == len(my_word2) - 1:
          isDone = False
        if my_word2[index] == '_' and other_word[index] in my_word2:
          Flag = False 
  return Flag
          
def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    lstwords = []
    for words in wordlist:
      if match_with_gaps(my_word, words, letters_guessed):
            lstwords.append(words) 
            #Output is bugged when '*' typed without any reveals (for example words with 4 chars is compromised of 2740 words)
            #file.write(words+ '\n')  Though, it is visible when written in file.  
    #CloseFile(file)
    return ' / '.join(lstwords)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
