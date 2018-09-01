import random 

rand_num = random.randint(0,2)
if rand_num == 0:
  computer = "rock"
elif rand_num == 1:
  computer = "paper"
else:
  computer = "scissors"


print('Rock!')
print('Paper!')
print('Scissors!')

player = input("Player, make your move: ").lower()

if player == computer: 
  print("You picked the same. It's a tie!")

elif player == "rock":
  if computer == "scissors":
    print("Player wins against scissors!")
  else:
    print("Computer wins with paper!")

elif player == "paper": 
  if computer == "rock":
    print("Player wins against rock!")
  else:
    print("Computer wins with scissors!")

elif player == "scissors":
  if computer == "paper":
    print("Player wins against paper!")
  else:
    print("Computer wins with rock!")

else: 
  print("Something went wrong. Maybe a typo?")
