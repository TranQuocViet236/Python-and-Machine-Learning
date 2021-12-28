import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            print(guess)
            if guess > random_number:
                if guess >= 10:
                    print("Sorry, guess number must be low than 10")
                print("To high!")
            elif guess < random_number:
                print("To low!")
            else:
                print(f"You win! You have guessed the number {random_number} correct!")
        except Exception as e:
            print("Error:"+ str(e))
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback !="c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} is too high (H), too low (L) or correctly(C)?")
        feedback = feedback.lower()
        if feedback == "h":
            high  = guess -1
        elif feedback == "l":
            low = guess +1
    print(f"Congratulations!The computer guessed you number, {guess}, correctly!")

# guess(10)
computer_guess(1000)