import random
"""def guess(x=int(input("You're guessing a number between 1 and: "))):
    random_number = random.randint(1,x)
    guessed= False
    while guessed is not(True):
        try:
            guessed_number = int(input("Enter your guess: "))
        except ValueError:
            print("Durrrr, that's the wrong input my friend")
        if guessed_number == random_number:
            guessed= True
        elif guessed_number > random_number:
            print(f"{guessed_number} is too high! Guess Again!")
        elif guessed_number < random_number:
            print(f"{guessed_number} is too low! Guess Again!")

    print("Congratulations! You guessed the right number!")
"""
def computer_guess(y=int(input("Give the computer a number to guess: "))):
    bottom = int(input("Bottom of the guessing range: "))
    top = int(input("Top of the guessing range: "))
    print(f"So im Guessing a number higher than {bottom}, but lower than {top}?")
    answer = input("Correct? (yes/no): ")
    comp_guess = int()
    while comp_guess != y and answer == "yes":
        comp_guess = random.randint(bottom,top)
        print("Gimme another try!")
    if comp_guess == y:
        print(f"HAH! Gotcha! Your number was {y}")
    elif answer == "no":
        print("You either put in the wrong numbers or are just wasting my damn time....")
computer_guess()