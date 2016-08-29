from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
# Create your views here.
global word,blanks,origuess,wrongGuess
global vowels,selectedChar,noOfHints
def index(request):
    global word,blanks,origuess,wrongGuess
    global vowels,selectedChar,noOfHints
    all_words = Words.objects.all()
    ind = random.randint(1,Words.objects.count())
    word = Words.objects.get(pk=ind).alpha
    vowels = ['a','e','i','o','u']  #used for hints
    selectedChar = []               #used for hints
    guess = ''
    blanks = 0
    wrongGuess = 1
    noOfHints = 3
    for char in word:
        asc = ord(char)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            guess += '_'
            blanks+=1
        else:
            guess += char
    origuess = guess
    context = {'guess':guess,'wrongGuess':str(wrongGuess),'answer':word,'hint':"",'noOfHints':int(noOfHints)}
    return render(request,'hang/index.html',context)


def game(request):
    global word,blanks,origuess,wrongGuess
    global selectedChar,noOfHints
    guess = origuess
    character = request.POST['guessed']
    flag = 0
    # if len(guess)!=len(word):
    #     return HttpResponse(guess)
    if character=='':
        wrongGuess+=1
        context = {'guess':guess,'wrongGuess':str(wrongGuess),'answer':word,'hint':"",'noOfHints':int(noOfHints)}
        return render(request,'hang/index.html',context)
    character = character[:1]
    selectedChar.append(character.lower())
    if blanks:
        asc = ord(character)
        if (ord('A')<=asc and ord('Z')>=asc) or (ord('a')<=asc and ord('z')>=asc):
            for i in xrange(0,len(word)):
                if (character.upper() == word[i] or character.lower() == word[i]) and guess[i]=='_':
                    guess = guess[:i] + word[i] + guess[i+1:]
                    blanks-=1
                    flag=1
        if flag==0:
            wrongGuess+=1
        if blanks:
            origuess = guess
            context = {'guess':guess,'wrongGuess':str(wrongGuess),'answer':word,'hint':"",'noOfHints':int(noOfHints)}
            return render(request,'hang/index.html',context)
    return HttpResponse(wrongGuess)

def hint(request):
    global word
    global selectedChar,vowels,noOfHints
    flag = 0
    hint = ''
    if(noOfHints>0):
        noOfHints-=1
        if vowels!=[]:
            ch=random.choice(vowels)
            while vowels!=[] and ch in selectedChar:
                vowels.remove(ch)
                if vowels!=[]:
                    ch = random.choice(vowels)
            if(vowels!=[]):
                if ch in word:
                    hint = "Word contains '"+ch+"'..."
                else:
                    hint = "Word does not contains '"+ch+"'..."
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
            hint = "Word contains '"+ch+"'..."
    context = {'guess':origuess,'wrongGuess':str(wrongGuess),'answer':word,'hint':hint,'noOfHints':int(noOfHints)}
    return render(request,'hang/index.html',context)



def add(request):
    fp = open('hang/tvshows.txt','r')
    lines = fp.readlines()
    #commented as they should not get added again
    # for line in lines:
    #     a = Words()
    #     a.alpha = line[:-1]
    #     a.save()
    return HttpResponse("Done!!!")
