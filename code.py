#!/usr/bin/python
import sys
import random
import re
from game import *


playOn = True
print "THE HANGMAN GAME!!!"
print "Can u guess the names of this Famous T.V. Shows!!!"
#Currently just supports Famous T.V. Shows
fp = open("tvshows.txt")
words = fp.readlines()          #all the words even have a '\n' at the end
donewith = []
while playOn:
    if len(donewith) == len(words): donewith=[]     # check if the all the words are covered
    sel = random.randint(0,len(words))
    while sel in donewith:
        sel = random.randint(0,len(words))
    donewith.append(sel)
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
    #function for main structure of game
    noOfGuess = game(word, guess, blanks)
    print "Total Number of Guesses required:-",noOfGuess
    dec = ''
    while (dec!='y' and dec!='n'):  dec=raw_input("Do you wish to play again?(y/n):")
    if dec=='n': playOn = False
