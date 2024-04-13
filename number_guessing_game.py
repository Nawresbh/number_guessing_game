import random 
def number_guessing_game():
    secret_number=random.randint(1,100)
    print("Welcome to the number guessing game ! :")
    print("I'm thinking of a number between 1 and 100 , can you guess what it is ?")
    max_guesses=6
    for guesses_taken in range(1,max_guesses+1):
        print("Take a guess (Attempt %d / %d ):"%(guesses_taken , max_guesses))
        guess=int(input())
        if (guess < secret_number):
            print("Your guess id too low ")
        elif(guess>secret_number):
            print("Your guess is too high")
        else :
            break
    if (guess==  secret_number):
        print("Good job you guesse my number in %d guesses"% (guesses_taken))
    else:
        print("Sorry the number I was thinking of was %d "% (secret_number))
number_guessing_game()
replay=input("Do you want to play again ? (yes/no):")
if (replay.lower()=="yes"):
    number_guessing_game()
else :
    print("thanks for playing ,Goodbye !")