name = input('What is your name? ')
print(f'Welcome {name} to your adventure!')

answer = input(
    'The road you are on has come to and end, you can go either left or right. Which way would you like to go? right/left ').lower()

if answer == 'right':
    answer = input(
        'You come to a town, you can walk around it or enter. Which do you choose? around/enter ').lower()
    if answer == 'enter':
        print(
            f'After entering the town, you were mistaken for a known bandit. Sorry {name}, but your journey has come to an end.')
    elif answer == 'around':
        print(
            f'While walking around the town, you come upon a chest of gold. Congradulation {name}, you have won!')
    else:
        print(f'Sorry {name}, but your journey has come to an end.')
elif answer == 'left':
    answer = input(
        'You come to a river, you can walk around it or swim across. Which do you choose? walk/swim ').lower()
    if answer == 'swim':
        print(
            f'While swimming across the river, you were attacked by an alligator. Sorry {name}, but your journey has come to an end.')
    elif answer == 'walk':
        print(
            f'While walking around the river, you were attacked by bandits. Sorry {name}, but your journey has come to an end.')
    else:
        print(f'Sorry {name}, but your journey has come to an end.')
else:
    print(f'Sorry {name}, but your journey has come to an end.')

print(f'Thank you for playing {name}!')
