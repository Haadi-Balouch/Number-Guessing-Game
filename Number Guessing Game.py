
import random as r
num = r.randint(1, 100)
attempts = 0
try:
    while True:
        guess = int(input('Enter your number between 1 and 100 or enter 0 to quit:'))
        if guess == 0:
            print('Thank you for playing the game.')
            break
        elif guess >100 or guess <1:
            raise ValueError('Please choose between 1 and 100')
        elif guess > num:
            print('Too High! Please choose a lower number')
            attempts += 1
        elif guess < num:
            print('Too Low! Please choose a higher number')
            attempts += 1
        elif guess == num:
            print(f"Congratulations! You have guessed the number in {attempts} attempts")
            break
except:
    print("Please choose a valid number between 1 and 100")