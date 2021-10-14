print('Welcome to my computer quiz!')

playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()

print('Okay, let\'s play!')

score = 0
answer = input('What does CPU stand for? ').lower()
if answer == 'centeral processing unit':
    score += 1
    print('Correct')
else:
    print('Incorrect')

answer = input('What does GPU stand for? ').lower()
if answer == 'graphics processing unit':
    score += 1
    print('Correct')
else:
    print('Incorrect')

answer = input('What does RAM stand for? ').lower()
if answer == 'random access memory':
    score += 1
    print('Correct')
else:
    print('Incorrect')

answer = input('What does PSU stand for? ').lower()
if answer == 'power supply unit':
    score += 1
    print('Correct')
else:
    print('Incorrect')

print(f'You got {score} questions correct!')
print(f'You got {round(score/ 4 * 100)}%')
