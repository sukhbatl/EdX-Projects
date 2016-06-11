# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\sukhbat.lkhagvadorj\Google Drive\EdX Python\Downloads\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    for char in secretWord:
        if char in lettersGuessed:
            # print char + ('is in lettersGuessed')
            result += 1
        else: print 'At least one character is not guessed yet!'
    return len(secretWord) == result



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for char in secretWord:
        if char in lettersGuessed:
            result += char
        else:
            result += '_'
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = set()
    alphabet = set(string.ascii_lowercase)
    for char in lettersGuessed:
        guessed.update(char)
    remained = alphabet - guessed
    remainedstring = ''
    for char in remained:
        remainedstring += char
    return remainedstring
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the Hangman made by Sukhbat!'
    print 'The secretWord contains ' + str(len(secretWord)) + ' characters.'
    print 'If you wish to stop this game at any point, please type in "stop!"'
    
    lettersGuessed = list()
    guessesLeft = 8
    print '----------------------------------------------'
    
    while guessesLeft > 0:
        print 'You have ' + str(guessesLeft) + ' guess(es) left.'
        print 'Available letters are: ' + getAvailableLetters(lettersGuessed)
        guessRaw = raw_input('Guess a letter: ')
        guess = guessRaw.lower()
        
        if guess == 'stop!':
            print 'This game has stopped as you requested.'
            break
        
        if len(guess) == 1 and guess in string.ascii_lowercase:
            if guess in lettersGuessed:
                print "Oops! You've already guessed that letter: " + \
                    str(getGuessedWord(secretWord, lettersGuessed)) 
                print 'Guessed letters are: ' + str(lettersGuessed)
                print '----------------------------------------------'       
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed += [guess]
                print 'Good guess: ' + str(getGuessedWord(secretWord,lettersGuessed))
                print 'Guessed letters are: ' + str(lettersGuessed)
                print '----------------------------------------------'
            if guess not in secretWord and guess not in lettersGuessed:
                lettersGuessed += [guess]
                print "Oops! That letter is not in my word: " + \
                    str(getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
                print 'Guessed letters are: ' + str(lettersGuessed)
                print '----------------------------------------------'
    
            if secretWord == str(getGuessedWord(secretWord, lettersGuessed)):
                print 'Congratulations, you won!'
                guessesLeft = 0
                print 'Enter "close" to close this game.'
                print 'Enter "restart" to play this game again.'         
                
                close = raw_input()
                if close == 'restart':
                    secretWord = chooseWord(wordlist).lower()
                    hangman(secretWord)
                if close == 'close':
                    break
    
            if guessesLeft == 0:
                print 'Sorry, you ran out of guesses. The secret word was ' + \
                    str(secretWord) + ' .'
                    
                print 'Enter "close" to close this game.'
                print 'Enter "restart" to play this game again.'                        
                close = raw_input()
                if close == 'restart':
                    secretWord = chooseWord(wordlist).lower()
                    hangman(secretWord)
                if close == 'close':
                    break


        else: 
            print 'Please enter a letter from the alphabet!'
            print '----------------------------------------------'
        
         
    
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
