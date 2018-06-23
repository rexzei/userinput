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

# Get lenght of array
wordArrayLengt = len(wordArray)

# Get random string from array using random.randrange
wordArrayNumber = random.randrange(0, wordArrayLengt)
wordArrayPrint = wordArray[wordArrayNumber]

# Get lenght of random string
wordArrayPrintLenght = len(wordArrayPrint)

# Defining attemptsLeft as a string
attemptsLeftToString = str(attemptsLeft)
attemptsLeftPhrase = "You have " + attemptsLeftToString + " attempts left"

# Defining attempts as a string
attemptsToString = str(wordArrayPrintLenght)
attemptsPhrase1 = "The word has " + attemptsToString + " characters"

print(wordArrayPrint)
print(wordArrayPrintLenght)

# Get userinput to userInput variable
while answer == 0:
    userInput = input("The word is: ")
    attemptsLeft = attemptsLeft - 1
    attempts = attempts + 1

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

print("Game end")
