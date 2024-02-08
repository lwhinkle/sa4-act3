number = 10
keep_going = True

while keep_going:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")

    if guess != 'q':
        guess = int(guess)

    if guess == number:
        keep_going = False
        print("Congratulations! You guessed the right number.")
    elif guess == 'q':
        keep_going = False
        print(f"The number was {number}.")
    else:
        if guess > number:
            print("Try guessing lower!")
        else:
            print("Try guessing higher!")
