import random
guess=random.randint(1,100)
number_of_attempts=0
while True:
    try:
        user_guess=int(input("Please enter a number to guess: "))
        if guess==user_guess:
            number_of_attempts=number_of_attempts+1
            print(f'You predicted correctly in {number_of_attempts} attempts.')
            break
        elif user_guess<guess:
            print('The number is low.Please choose a higher number: ')
            number_of_attempts=number_of_attempts+1
        else:
            print('The number is high.Please select a lower number: ')
            number_of_attempts=number_of_attempts+1
    except:
        print('Please choose a number between 1 and 100')
            