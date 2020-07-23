# secret number game
import random
secret_number = random.randint(1, 100)

NUM = 0

while NUM != secret_number:
    NUM = int(input("Guess a number between 1 - 100: "))

    if NUM > secret_number:
        print('NUM is larger than secret number.')

    elif NUM < secret_number:
        print('NUM is less than secret number.')


    elif NUM == secret_number:
        print('NUM is the secret_number')
        print('You win!')
        break