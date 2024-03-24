'''Group 13 Sebastian Rosas and Saiah Montoya
This program allow sthe user to play as a Hero and explore a dungeon maze, filled with different monsters, and the hero must fight them all as they explore the maze. The user will win the game if they reach the end of the dungeon, but will lose if the Hero runs out of HP. '''
import random
import Map
import Enemy
import Hero
import check_input

def main():
  name = input('What is your name? ')
  player = Hero.Hero(name)
  game_map = Map.Map()
  game_finished = False
  game_map.reveal(player.loc)

  '''Game Loop'''
  while game_finished == False:
    if player.hp == 0:
      print('You lose')
      break
    print('\n'+str(player)+'\n')
    game_map.show_map(player.loc)

    '''Asks the user if they'd like to travel North South East or West'''
    print('\n1. Go North\n2. Go East\n3. Go South\n4. Go West\n')
    player_input = check_input.get_int_range('Enter input: ',1,4)

    if player_input == 1:
      loc_contents = player.go_north()
    if player_input == 2:
      loc_contents = player.go_east()
    if player_input == 3:
      loc_contents = player.go_south()
    if player_input == 4:
      loc_contents = player.go_west()

    game_map.reveal(player.loc)

    '''M Reveals monster'''
    if loc_contents == 'M':
      enemy = Enemy.Enemy()
      print('\nYou found a '+ enemy.name+'\n')

      '''Displays the options of Attack or Run away'''
      while enemy.hp != 0:
        print(enemy)
        print('\n1. Attack\n2. Run away\n')
        player_input = check_input.get_int_range('Enter input: ',1,2)

        
        
        if player_input == 1:
           print('\n'+player.attack(enemy))
          
        if player_input == 2:
          print('\nYou ran away.\n')
          escape = random.randint(1,4)
          
          if escape == 1:
            player.go_north()
          if escape == 2:
            player.go_east()
          if escape == 3:
            player.go_south()
          if escape == 4:
            player.go_west()
          game_map.reveal(player.loc)
          break

        '''If the enemy's HP reaches 0 they died, if not the enemy will attack the player'''
        if enemy.hp == 0:
          print('\nThe '+enemy.name+' died.')
          game_map.remove_at_loc(player.loc)
        else:
          print('\n'+enemy.attack(player))

    '''Location Contents displayed mean different things. 
    X = Out of bounds
    N = Room is empty
    S = Start of the dungeon
    I = Healing Potion
    F = Escape Dungeon
    '''
    if loc_contents == 'X':
      print('\nOut of Bounds')
    if loc_contents == 'N':
      print('\nLooks like this rooms empty.')
    if loc_contents == 'S':
      print('''\nLooks like you're back at the start of the dungeon.''')
    if loc_contents == 'I':
      print('\nLooks like you found a healing potion. You healed to full health.')
      player.heal()
      game_map.remove_at_loc(player.loc)
    if loc_contents == 'F':
      print('\nYou escaped the dungeon!')
      game_finished = True

main()
    

          
        
      
    

    
