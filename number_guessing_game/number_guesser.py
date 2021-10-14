import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please input a number greater than zero next time.')
        quit()
else:
    print('Please input a number next time.')
    quit()

random_mumber = random.randint(0, top_of_range)
# print(random_mumber)

guesses = 0
while True:
    guesses += 1
    user_guess = input('Guess a number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please input a number next time.')
        continue

    if user_guess == random_mumber:
        print('You got it right.')
        print(f'You got it in {guesses} guesses.')
        break
    elif user_guess < random_mumber:
        print('Guess higher')
    else:
        print('Guess lower')
