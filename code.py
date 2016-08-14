#!/usr/bin/python
import sys
import random
import re

playOn = True
print "THE HANGMAN GAME!!!"
print "Can u guess the names of this Famous T.V. Shows!!!"
#Currently just supports Famous T.V. Shows
fp = open("tvshows.txt")
words = fp.readlines()          #all the words even have a '\n' at the end
while playOn:
    sel = random.randint(0,len(words))
    word = words[sel][:-1]              #skip '\n'
    guess = ''
    blanks = 0
    for char in word:
        asc = ord(char)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            guess += '_'
            blanks+=1
        else:
            guess += char
    print guess
    # print word
    print "\nSo start guessing the name"
    noOfGuess = 0
    while blanks:
        character = ''
        while (character==''):  character=raw_input("Enter a character(case insensitive):-")[0]
        noOfGuess+=1
        asc = ord(character)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            for i in xrange(0,len(word)):
                if (character.upper() == word[i] or character.lower() == word[i]) and guess[i]=='_':
                    guess = guess[:i] + word[i] + guess[i+1:]
                    blanks-=1
        print guess
    print "Total Number of Guesses required:-",noOfGuess
    dec = ''
    while (dec!='y' and dec!='n'):  dec=raw_input("Do you wish to play again?(y/n):")
    if dec=='n': playOn = False
