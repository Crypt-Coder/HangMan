#!/usr/bin/python
def game(word,guess,blanks):
    noOfGuess = 0
    while blanks:
        character = ''
        while (character==''):  character=raw_input("Enter a character(case insensitive):-")
        character = character[:1]
        noOfGuess+=1
        asc = ord(character)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            for i in xrange(0,len(word)):
                if (character.upper() == word[i] or character.lower() == word[i]) and guess[i]=='_':
                    guess = guess[:i] + word[i] + guess[i+1:]
                    blanks-=1
        print guess
    return noOfGuess
