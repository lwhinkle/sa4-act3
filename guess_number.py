number = 10
keep_going = True
num_guesses = 3

while keep_going:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")

    if guess != 'q':
        guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the right number.")
    elif guess == 'q':
        keep_going = False
        print(f"The number was {number}.")
    else:
        num_guesses = num_guesses - 1
        if num_guesses == 0:
            keep_going = False
            print(f"Sorry! You ran out of guesses. The number was {number}.")
        else:
            print(f"Incorrect. You have {num_guesses} left.")
