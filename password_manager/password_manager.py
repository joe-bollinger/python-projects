from cryptography.fernet import Fernet

# master_password = input('What is your master password? ')

'''
USED ONE TIME ONLY!!!
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


write_key()
'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
f_key = Fernet(key)


def add():
    name = input('What is your name? ')
    pwd = input('What is your password? ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + f_key.encrypt(pwd.encode()).decode() + '\n')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, pwd = data.split('|')
            print(
                f'User: {user}, Password: {f_key.decrypt(pwd.encode()).decode()}')


while True:
    mode = input(
        'Would you like to add a new password or view an existing password? view/add/quit ').lower()

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    elif mode == 'quit':
        break
    else:
        print('Invalid mode, please try again.')
        continue
