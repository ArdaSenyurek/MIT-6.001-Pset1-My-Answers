import string

a = 'apple'
b = ['e', 'i', 'k', 'p', 'r', 's']

def is_word_guessed(secret_word, letters_guessed):
   
    counter = 0
    secret_word = str.lower(secret_word)
    for i in letters_guessed:
        letters_guessed[counter] = str.lower(i)
        counter += 1
    print(letters_guessed)
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
    #print(letters_guessed)
    #print(secret_word)
    return secret_word

def get_guessed_word(secret_word, letters_guessed):
    
    str_lower(secret_word,letters_guessed)
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
    #print(temp)
    return ''.join(temp)

def get_available_letters(letters_guessed):
    
    ascii_low = string.ascii_lowercase
    lst_ascii_low = list(ascii_low)
    for letter in letters_guessed:
        if letter in string.ascii_lowercase:
            lst_ascii_low.remove(letter)
    return ''.join(lst_ascii_low)

print (get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) =='abcdfghjlmnoqtuvwxyz' )