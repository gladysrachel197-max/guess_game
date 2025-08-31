import random
print("=== Number Guessing Game ===")
secret = random. randint(1, 10)   # computer picks a number 1..10
attempts = 0                      # start counting tries

while True:
    guess_text = input("Guess a number between 1 and 10:")
    if not guess_text.isdigit():
        print("Please type a NUMBER between 1 and 10")
        continue
    guess = int(guess_text)
    attempts += 1                 

    if guess < secret:
        print("Too low.")
    elif guess > secret:
         print("Too high.")
    else:
         print(f"Correct! You guessed it in {attempts} tries")
         break   # exit the loop when correct
