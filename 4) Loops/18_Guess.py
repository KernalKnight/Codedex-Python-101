tries = 0
guess = 0

while guess != 6 and tries < 3:
    guess = int(input("Guess the number: "))
    tries += 1

if guess != 6:
    print("Better luck next time!")
else:
    print("You got it!")