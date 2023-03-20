# Constants
import random

DICTIONARY = open("/Users/preethamyerragudi/english-words/words.txt", "r")
WORD_SIZE = 10
GUESS_LIMIT = 9

# Variables
lost = True
words_guessed = []
word = "-"*WORD_SIZE
guesses = 0
listOfPossibleWords = [i.lower() for i in DICTIONARY if len(i) - 1 == WORD_SIZE]

while guesses < GUESS_LIMIT:
    if len(listOfPossibleWords) == 1 and word == listOfPossibleWords[0]:
        print("Congrats, you guessed the word!")
        lost = False;
    stage = -1
    print("Words Guessed: "+str(words_guessed))
    guess = input(str(GUESS_LIMIT - guesses) + " guesses left: ")
    if(guess == "PREETHAMISREALLYCOOL"):
        print(listOfPossibleWords)
        print("\nThis is my gift to you for speaking straight facts\n")
        continue
    elif len(guess) > 1:
        print("ERROR: Not a single charecter")
        continue
    elif guess in words_guessed:
        print("ERROR: Already Guessed")
        continue
    words_guessed+=guess
    numWithoutLetter = [x for x in listOfPossibleWords if guess not in x]
    for num in range(WORD_SIZE):
        potential = [x for x in listOfPossibleWords if x[num] == guess and guess not in (x[:num] + x[num+1:])]
        if len(potential) > len(numWithoutLetter):
            numWithoutLetter = potential
            stage = num
    if not stage == -1:
        print(guess+" was in the word")
        word = word[:stage] + guess + word[stage + 1:]
    else:
        print(guess+" was not in the word")
        guesses += 1

    listOfPossibleWords = numWithoutLetter
    #print(listOfPossibleWords)
    print(word)
if lost:
    print("The word was "+listOfPossibleWords[random.randrange(0,len(listOfPossibleWords))])
