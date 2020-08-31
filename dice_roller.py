import random

def main():
  player_size = int(input('Enter how many players (1-8): '))
  if player_size < 1:
    player_size = 1
  if player_size > 8:
    player_size = 8
  player_list = []
  for i in range(player_size):
    player_list.append(input("Enter name of player: "))
  dice_size = int(input('How many sides are the dice? '))
  dice_rolls = int(input('How many dices would you like to roll? '))

  for play in player_list:
    print(play," is playing now . . .")
    dice_sum = 0
    for i in range(dice_rolls):
      roll = random.randint(1,dice_size)
      dice_sum += roll
      if roll == 1:
        print(f'{play} rolled a {roll}:Critical Fail')
      elif roll == dice_size:
        print(f'{play} rolled a {roll}:Critical Success')
      else:
        print(f'{play} rolled a {roll}')
    print(f'{play} has rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
