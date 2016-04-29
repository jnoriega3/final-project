import random

from random import shuffle

words=("github", "shell", "bacon", "variables", "boolean values", "operators", "functions", "lists", "the none value", "global scope", "for and while loops", "in and not operators")

#Codinng Joke (meant for word scramble ...My code is not working, I have no idea why---My code works, I have know idea why!
print()

print('.............Welcome to Words with Coders..........')
print()

print('.....Brought to you by the 2016 Valencia Automaters......')

print()

play=input("   ..Do you want to play? (yes, no, or enter to quit)")

while play=="yes":
    word=random.choice(words)
    correct=word

    scramble=""
    while word:
        position = random.randrange(len(word))
        scramble += word[position]
        word = word[:position] + word[(position + 1):]

    print()
    print("Your scramble is:", scramble)
    points=100

    guess=input("\nYour Guess:")
    while guess != correct and guess !="":
        print()
        print()
        print("Guess again!")
        print()
        print("Really? You can't figure it out?")
        guess = input("Your guess:")
    if guess == correct:

        print("Exactly right!!\n")

        print("And your final score is..."+str(points))
                           
        print()
        play=input("   ..Do you want to play? (yes, no, or enter to quit)")
        print()
        print("thanks for hanging Python Master!")
        
    input("]\n\nI hope you enjoyed the praced on the word with Python. Presss the enter key to exit. Come back soon!")
    
          
