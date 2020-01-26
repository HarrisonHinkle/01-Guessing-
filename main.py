import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
quit = False
high_score = 100
guess = -1 
while not quit:
    answer = random.randint(1,20)
    
    count = 0
    while guess != answer: 
        guess = input("Please guess a number between 1 and 20: ")
        if not guess.isdigit():
            print("You must guess a number")
        else:   
            guess = int(guess)
            if int(guess) > answer:
                print("Sorry you didn't get it right")
                print("Too high")
            elif int(guess) < answer:
                print("Sorry you didn't get it right")
                print("Too low")
            count = count + 1
    print("Good job")
    print("You guessed it in", count, "tires")

    if count < high_score:
        high_score = count
        print("New High Score!")
    else:
        print("Your high score is", high_score)
    again = input("Would you like to try again? ")    
    if again == "yes" or again == "y":
        quit = False
    else:
        quit = True
print("Thank you for playing. Your final high score is", high_score)