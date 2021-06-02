"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    secret_word=secret_word.strip()
    l=len(secret_word)
    print(l)
    d=""
    for i in range(l):
        d=d+"-"
    print("The word now looks like this: "+d)
    print("You have 8 guesses left")
    n=8
    c=0
    l=[]
    k=-1
    while n>0:
     s=input("Type a single letter here, then press enter: ")
     s=s.upper()
     if s in secret_word:
         l.clear()
         k=-1
         for i in secret_word:
             k=k+1
             if i==s:
                c=c+1
                l.append(k)
                
         k=-1   
         
         if c==1:       
            print("That guess is correct.")
            res=secret_word.index(s)
            w=list(d)
            w[res]=s
            d="".join(w)
            if d==secret_word:
                print('Congratulations, the word is: '+secret_word)
                n=0
            else:    
                print("The word now looks like this: "+d)
                print('You have {} guesses left'.format(n))
            c=0

         else:
             print('That guess is correct.')
             for i in range(c):
                 w=list(d)
                 w[l[i]]=s
                 d=''.join(w)
             if d==secret_word:
                 print('Congratulations, the word is: '+secret_word)
                 n=0
             else:    
                print("The word now looks like this: "+d)
                print('You have {} guesses left'.format(n))
             c=0
       

     else:
            print("There are no {}'s in the word".format(s))
            n=n-1
            if n!=0:
              print('You have {} guesses left'.format(n))
            else:
              print('Sorry, you lost. The secret word was: '+secret_word)

        







def get_word():
    
    """ This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'"""
    f = open("Lexicon.txt", "r")
    l=[]
    for x in f:
        l.append(x)
    index=random.randrange(100)
    return l[index]
    f.close()
        




def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
