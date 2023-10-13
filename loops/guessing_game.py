def guessing_game():
    secret_word = "rofina"
    guess = ""
    guess_limit = 4
    guess_count = 0
    out_of_guesses = False

    while  guess != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ") 
            guess_count += 1
        else:
            out_of_guesses = True
            
    if  out_of_guesses:
        print("Out of guesses, You lose!")
    else:
        print("You got it")

guessing_game()