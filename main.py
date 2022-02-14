import random

nnn = int(random.randint(0,4))
fn = input('Enter First Name: ')
ln = input('Enter Last Name: ')
nn = ['The Cyberpunk', 'The Engineer', 'The Hacker', 'The Computer Programmer', 'The Elite']
full_name = (f'{fn} "{nn[nnn]}" {ln}')

while True:
    print('Main Menu: ' + full_name)
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    answer = int(input('Enter Number Here: '))
    if answer == 1:
        fn = input('Enter First Name: ')
        ln = input('Enter Last Name: ')
        full_name = (f'{fn} "{nn[nnn]}" {ln}')
    elif answer == 2:
        nnn_r = int(random.randint(0, len(nn) - 1))
        full_name = (f'{fn} "{nn[nnn_r]}" {ln}')
    elif answer == 3:
        for i in range(len(nn)):
            print(nn[i])
    elif answer == 4:
        nn.append(input('Enter New Nickname: '))
    elif answer == 5:
        # If the nickname deleted is the current nickname, then it will remain that way until a new nickname is chosen
        remove = int(input('Which Nickname would you like to delete? Please give a number '))
        nn.pop(remove - 1)
        print(f'Removed {nn[remove - 1]} from the nickname list')
    elif answer == 6:
        break


