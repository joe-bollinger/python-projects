import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Quit: ').lower()
    if user_input == 'quit':
        break
    if user_input not in options:
        continue
    random_mumber = random.randint(0, 2)
    # rock = 0 paper = 1 scissors = 2
    computer_pick = options[random_mumber]
    print(f'Computer picked: {computer_pick}')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You win!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You win!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You win!')
        user_wins += 1
    elif user_input == computer_pick:
        print('You tied!')
    else:
        print('You lost!')
        computer_wins += 1

print(f'You won {user_wins} times!')
print(f'The computer won {computer_wins} times!')

print('Goodbye')
