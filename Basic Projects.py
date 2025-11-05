print("Guessthenumber")


import random

secretnumber = random.randint(1, 12)
print('I am thinking of a numbre between 1 and 12')

guess = input('Your guess is ')
guess = int(guess)

def ask(guess):
    while guess != secretnumber:
        if guess < secretnumber:
            print('Guess again too low')
        elif guess > secretnumber:
            print('Guess again too high')
        print('Congrats')


import random

def play_game():
    
    secretnumber = random.randint(1, 12)
    print('I am thinking of a numbre between 1 and 12')

    guess = int(input('Your guess is: '))

    while guess != secretnumber:
        if guess < secretnumber:
            print('Guess again too low')
        elif guess > secretnumber:
            print('Guess again too high')
        
        # Ask for a *new* guess INSIDE the loop
        guess = int(input('Your guess is: '))

    print('Congrats')


play_game()


#computer guesses the number

def computerguess(num): 
    min = 1
    max = num
    feedback = ''
    while feedback != 'correct':
        compguess = random.randint(min, max)
        feedback = input(f'is {compguess} too high, too low or correct?')
        if feedback == 'high':
            max = compguess - 1
        elif feedback == 'low':
            min = compguess + 1
    
    print(f'yay got it its {compguess}')
        

    
    



