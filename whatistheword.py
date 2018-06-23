# Import

import random

# Boolean
answer = 0

# AttemptsLeft int
attemptsLeft = 5

# Attempts
attempts = 0

# Array
wordArray = ["apple", "orange", "melon", "kiwi"]
colorArray = ["red", "orange", "yellow", "green"]

# Get lenght of array
wordArrayLengt = len(wordArray)

# Get random string from array using random.randrange
wordArrayNumber = random.randrange(0, wordArrayLengt)
wordArrayPrint = wordArray[wordArrayNumber]

# Match colorArray with wordArray
colorArrayPrint = colorArray[wordArrayNumber]

# Get lenght of random string
wordArrayPrintLenght = len(wordArrayPrint)

# Get first character of random string
wordArrayPrintOneCharacter = wordArrayPrint[:1]
wordArrayPrintTwoCharacter = wordArrayPrint[:2]
wordArrayPrintThreeCharacter = wordArrayPrint[:3]

# Defining attemptsLeft as a string
attemptsLeftToString = str(attemptsLeft)
attemptsLeftPhrase = "You have " + attemptsLeftToString + " attempts left"

# Defining attempts as a string
attemptsToString = str(wordArrayPrintLenght)
attemptsPhrase1 = "The word has " + attemptsToString + " characters"

# colorArray into a phrase
colorArrayPhrase = "The color can be " + colorArrayPrint

print(wordArrayPrint)
print(wordArrayPrintLenght)

# User Input
while answer == 0:
    userInput = input("The word is: ")
    attemptsLeft = attemptsLeft - 1
    attempts = attempts + 1

    # Updating attemptsLeftPhrase
    attemptsLeftToString = str(attemptsLeft)
    attemptsLeftPhrase = "You have " + attemptsLeftToString + " attempts left"

    if userInput == wordArrayPrint:
        answer = 1
        print("Nice!")
        break

    elif attempts > 5:
        break

    else:
        print(attemptsLeftPhrase)
        answer = 0
        if attempts == 1:
            print(attemptsPhrase1)
        elif attempts == 2:
            print(wordArrayPrintOneCharacter)
        elif attempts == 3:
            print(wordArrayPrintTwoCharacter)
        elif attempts == 4:
            print(wordArrayPrintThreeCharacter)
        elif attempts == 5:
            print(colorArrayPhrase)

print("Game end")
