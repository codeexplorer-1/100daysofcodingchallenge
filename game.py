import random
def play():
  user_choice = input("Enter 'Rock' (R), 'Paper' (P), or 'Scissors' (S): ").upper()
  computer_choice = random.choice(['R', 'P', 'S'])
  user_choice = user_choice[0]
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == 'R' and computer_choice == 'S') or \
       (user_choice == 'P' and computer_choice == 'R') or \
       (user_choice == 'S' and computer_choice == 'P'):
    print("You win!")
  else: print("You lose.")
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")
while True:
  play()
  play_again = input("Play again? (y/n): ").lower()
  if play_again != 'y':
    break
if __name__ == "__main__":
  print("Welcome to Rock, Paper, Scissors!")
  play()
