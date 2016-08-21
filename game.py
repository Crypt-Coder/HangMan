#!/usr/bin/python
import random


def game(word,guess,blanks):
    noOfGuess = 0
    selectedChar = []
    #declared here so the hints do not get repeated
    vowels = ['a','e','i','o','u']
    noOfHints = 3
    while blanks:
        character = ''
        while (character==''):  character=raw_input("Enter a character(case insensitive):-")
        if character.lower() == 'skip':
            return -1
        if character.lower() == 'hint':
            if noOfHints:
                vowels = hint(selectedChar,word.lower(),vowels)
                print guess
                noOfHints-=1
            else:
                print "Sorry you have no hints left :("
            continue
        if character.lower() == 'quit':
            exit()
        character = character[:1]
        selectedChar.append(character.lower())
        noOfGuess+=1
        asc = ord(character)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            for i in xrange(0,len(word)):
                if (character.upper() == word[i] or character.lower() == word[i]) and guess[i]=='_':
                    guess = guess[:i] + word[i] + guess[i+1:]
                    blanks-=1
        print guess
    return noOfGuess

def hint(selectedChar,word,vowels):
    flag = 0
    if vowels!=[]:
        ch=random.choice(vowels)
        while vowels!=[] and ch in selectedChar:
            vowels.remove(ch)
            if vowels!=[]:
                ch = random.choice(vowels)
        if(vowels!=[]):
            if ch in word:
                print "Word contains '",ch,"'..."
            else:
                print "Word does not contains '",ch,"'..."
            vowels.remove(ch)
            flag = 1
    if flag==0:
        consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        temp = list(''.join([l for l in word.strip() if l in consonents]))
        ch=random.choice(temp)
        while temp!=[] and ch in selectedChar:
            temp.remove(ch)
            if temp!=[]:
                ch = random.choice(temp)
        print "Word contains '",ch,"'..."
    return vowels
