instructions = """
This will be our tic tac toe board
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 


*instructions:
1. Insert the spot number(1-9) to put your sign,
2. You must fill atleast 5 spots to get result,
3. Player 1 will go first.
"""

spots = []

for i in range(9):
  spots.append(' ')


def print_board(spots):
  board = f"""
   {spots[0]} | {spots[1]} | {spots[2]}
  ---|---|---
   {spots[3]} | {spots[4]} | {spots[5]}
  ---|---|---
   {spots[6]} | {spots[7]} | {spots[8]}
  """
  print(board)


index_list = []
def take_input(player_name):
  while True:
    x = int(input(f'{player_name}: '))
    x -= 1
    if 0 <= x < 9:
      if x in index_list:
        print('This spot is blocked.')
        continue
      index_list.append(x)  
      return x
    print('Please Enter number between 1-9')

def cal1(spots):

    for i in range(3):
        if spots[i * 3] == spots[i * 3 + 1] == spots[i * 3 + 2]:
            return spots[i * 3]
        if spots[i] == spots[i + 3] == spots[i + 6]:
            return spots[i]

    if spots[0] == spots[4] == spots[8]:
        return spots[0]
    if spots[2] == spots[4] == spots[6]:
        return spots[2]


def result(player_one,player_two,count):
    m=cal1(spots)

    if count==9:
      print("Match is Draw !!")
      return True

    elif count > 5:    
      if m=="X":
        print(player_one, "you are the winner!! ")
        return True
      elif m=="O":
        print(player_two, "you are the winner!! ")
        return True

    return False


def main():
  count = 1;
  print("Welcome to Shashank's tic tac toe game.!!")
  player_one = input("Enter player 1 name: ")
  player_two = input("Enter player 2 name: ")
  print("Thank you for joining",player_one, "and", player_two)
  print(instructions)
  print(player_one,"your sign will be - X")
  print(player_two,"your sign will be - O")
  input("Enter any key to start the game: ")
  print_board(spots)

  for i in range(0,9):
    if i%2 == 0:
      index = take_input(player_one)
      spots[index] = 'X'
      count += 1
    else:
      index = take_input(player_two)
      spots[index] = 'O'
      count += 1
    print_board(spots)
    res = result(player_one,player_two,count)
    if res == True:
        break




main()
