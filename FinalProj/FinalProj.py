import string, random

def passGen(length):
    if length < 8:
        source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        source = list(source)
        random.shuffle(source)
        finalPass = random.choices(source, k=8)
        finalPass = ''.join(finalPass)
        print('The recommended length for a password is 8 characters.')
        print('Your recommended password is', finalPass)

    source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    source = list(source)
    random.shuffle(source)
    finalPass = random.choices(source, k=length)
    finalPass = ''.join(finalPass)
    print('Your password is', finalPass)
def userInput():
    while True:
        try:
            length = int(input('How many characters do you want?: '))
            if length < 0:
                print('Please enter a postive integer')
                continue
            passGen(length)
            break
        except ValueError:
            print('Please enter an integer')
            continue

def askAgain():
    while True:
        ans = input('Do you want to try again? y/n: ')
        if ans.lower() == 'y':
            userInput()
        elif ans.lower() == 'n':
            break
        else:
            print('Please only use "y" or "n"')
            continue

def main():
    print('Welcome to the Password Generator!')
    userInput()
    askAgain()

if __name__ == "__main__":
    main()


