secrete_word = "rofina"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secrete_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ") 
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose")    
else :    
    print("You got it")