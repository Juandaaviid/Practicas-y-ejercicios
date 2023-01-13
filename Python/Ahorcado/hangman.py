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

WORDLIST_FILENAME = "words.txt"


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
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
  auxiliar = 0
  for i in range(len(letters_guessed)):
    if letters_guessed[i] in secret_word:
      auxiliar += 1
  if auxiliar == len(secret_word):
    return True
  else:
    return False




def get_guessed_word(secret_word, letters_guessed):
  resultado = []
  for i in secret_word:
    if i in letters_guessed:
      resultado.append(i)
    else:
      resultado.append("_ ")
  return "".join(resultado)




def get_available_letters(letters_guessed):
    abecedario = string.ascii_lowercase
    aux = []
    for i in abecedario:
      if i not in letters_guessed:
        aux.append(i)
    return "".join(aux)

    
    

def hangman(secret_word):
  print("Bienvenido al juego")
  print("estoy pensando en una palabra de", len(secret_word), "letras")
  intentos = 0
  Letrasadivinadas = []
  while 8 - intentos > 0:
    print(Letrasadivinadas)
    print("------------")
    print("Tiene", 8 - intentos, "restantes")
    print("letras disponibles: ", get_available_letters(Letrasadivinadas))
    entrada = str(input("Por favor ingrese una letra: ")).lower()
    if entrada in secret_word and entrada not in Letrasadivinadas:
      Letrasadivinadas.append(entrada)
      print("Buen intento: ", get_guessed_word(secret_word, Letrasadivinadas))
    elif entrada in Letrasadivinadas:
      print("letra repetida:", get_guessed_word(secret_word, Letrasadivinadas))
    elif entrada not in secret_word:
      print("esa letra no esta en la palabra: ", get_guessed_word(secret_word, Letrasadivinadas))
      Letrasadivinadas.append(entrada)
      intentos += 1
    if is_word_guessed(secret_word, Letrasadivinadas) == True:
      print("------------")
      print("Felicidades, ganoo")
      break
    if 8 - intentos == 0:
      print("------------")
      print("Lo siento, no hay mas oportunidades, la palabra es: ", secret_word)
      break
    else:
      continue



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  num = 0
  my_word = my_word.replace(' ', '')
  if len(my_word) == len(other_word):
    for i in range(len(my_word)):
      if my_word[i] == '_' or my_word[i] == other_word[i]:
        pass
      else:
        num += 1
    if num == 0:
      return True
    else:
      return False
  else:
    return False



def show_possible_matches(my_word):
  lista = []
  for word in wordlist :
    if match_with_gaps(my_word, word) == True :
      lista.append(word)
  cadena = " ".join(lista)
  print(cadena)



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
    
    #secret_word = choose_word(wordlist)
    #secret_word = "papel"
    #hangman(secret_word)
    secret_word = 'moon'
    letters_guessed = ['o', 'm', 'n', 'r', 'k', 'o']
    print(is_word_guessed(secret_word, letters_guessed))



###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)