'''
Group 13 9/28/22 Sebastian Rosas and Saiah Montoya. 
This program allows a player to play a game of Yahtzee with 3 dice. The user will be prompted to "roll" a set of dice. The results from the dice are created with a Dice class, generating a random value for each roll. If the user gets a matching pair they will recieve 1 point. If the user gets a series they will get 2 points. If the user gets 3 of a kind, they will get 3 points. The score is added up for every game played. The game is over whenever the user decides to stop playing.
'''

import Player
import check_input

def take_turn(player):
  player.roll_dice()
  print(player)

  '''check dice results'''
  if player.has_pair() == True:
    print('You got a Pair!\n')
    
  elif player.has_3_of_a_kind() == True:
    print('You got three of a kind!\n')
    
  elif player.has_series() == True:
    print('You got a series!\n')
    
  else:
    print('Sorry you lose.\n')

  print('Score: '+str(player.points)+'\n')
  

def main():
  user = Player.player()
  y_n_input = True
  print('_Yahtzee_')

  '''rolling dice loop'''
  while y_n_input == True:
    take_turn(user)
    y_n_input = check_input.get_yes_no('Play again? (Y/N): ')

  print('\nGame Over. Final Score: '+str(user.points))

main()
  
  