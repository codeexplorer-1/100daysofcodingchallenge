def display_board(board):
  for i in range(3):
    for j in range(3):
      print(board[i*3 + j], end=" ")
    print()

def is_valid_move(board, position):
  return board[position] == " "

def make_move(board, player, position):
  board[position] = player

def has_won(board, player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for row in win_conditions:
    if all(board[i] == player for i in row):
      return True
  return False

def is_board_full(board):
  return not any(cell == " " for cell in board)

def main():
  board = [" " for _ in range(9)]
  current_player = "X"
  game_on = True

  while game_on:
    display_board(board)

    while True:
      try:
        position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if 0 <= position <= 8 and is_valid_move(board, position):
          break
        else:
          print("Invalid move. Try again.")
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")

    make_move(board, current_player, position)
    current_player = "O" if current_player == "X" else "X"

    if has_won(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      game_on = False
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      game_on = False

if __name__ == "__main__":
  main()
