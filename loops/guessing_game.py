def guessing_game():
    secrete_word = "rofina"
    guess = ""
    guess_count = 0
    guess_limit = 4
    out_guesses = False

    while guess != secrete_word and not(out_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess")
            guess_count += 1
            out_guesses = True
    if out_guesses:
        print("Out off guess, You lose!")
    else:
        print("You got it")


guessing_game()
