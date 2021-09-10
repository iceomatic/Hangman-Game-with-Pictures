import random
from Hangman_Pics import pic
my_wordlist = []
with open("english_words.txt") as f:
    for word in f:
        my_wordlist.append(word.strip())

def hangman():
    i= 0
    underlines_array = []
    display_underlines = ""
    guess_count = 0
    secret_word = random.choice(my_wordlist)
    lost = False
    for letter in secret_word:
        underlines_array.append("_")
    display_underlines = "".join(underlines_array)
    while display_underlines != secret_word and lost != True:
        pic(guess_count)
        print(display_underlines)
        guess = input("Guess a letter: ")
        for letter in secret_word:
            if guess in letter:
                underlines_array[i] = guess
            if i < len(secret_word)-1:
                i += 1
            elif i == len(secret_word)-1:
                i=0
        if guess not in secret_word:
            if guess_count < 8:
                guess_count += 1
                print(f"Try Again, you have {8-guess_count} guesses left. ")
                if guess_count == 8:
                    lost = True

        display_underlines = "".join(underlines_array)
        if guess == secret_word:
            display_underlines = secret_word

    if lost == True:
        pic(8)
        print(f"Too bad, you've lost. The word was {secret_word}...\nBetter Luck Next Time!\nPress Ctrl+Shift+F10 to restart :)")
    else:
        print(f"Congratulations! You've Won!\nThe word was {secret_word}!")
hangman()

