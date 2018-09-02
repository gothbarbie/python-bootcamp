import random 

random_number = random.randint(1,10)
guess = None
guesses = 0

while guess != random_number:
  guess = input("Pick a number between 1 and 10: ")
  guesses += 1 
  guess = int(guess)
  if guess < random_number:
    print("Too low...")
  elif guess > random_number: 
    print("Too high...")
  else:
    print(f"Congratulations! You guessed right with {guesses} guesses. You won!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
      random_number = random.randint(1,10)
      guess = None
      guesses = 0
    else: 
      print("Thanks for playing!")
      break


