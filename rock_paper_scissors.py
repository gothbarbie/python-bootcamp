from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

print('Rock!')
print('Paper!')
print('Scissors!')

while player_wins < winning_score and computer_wins < winning_score:

  player = input("First to 3 wins! Player - make your move: ").lower()
  
  if player == "quit" or player == "q":
    break

  rand_num = randint(0,2)

  if rand_num == 0:
    computer = "rock"
  elif rand_num == 1:
    computer = "paper"
  else:
    computer = "scissors"

  if player == computer: 
    print("You picked the same. It's a tie!")

  elif player == "rock":
    if computer == "scissors":
      print("Player wins against scissors!")
      player_wins += 1
    else:
      print("Computer wins with paper!")
      computer_wins += 1

  elif player == "paper": 
    if computer == "rock":
      print("Player wins against rock!")
      player_wins += 1
    else:
      print("Computer wins with scissors!")
      computer_wins += 1

  elif player == "scissors":
    if computer == "paper":
      print("Player wins against paper!")
      player_wins += 1
    else:
      print("Computer wins with rock!")
      computer_wins += 1


  else: 
    print("Something went wrong. Maybe a typo?")


print(f"Thanks for playing! Final scores: \n Player: {player_wins}\n Computer: {computer_wins}")
