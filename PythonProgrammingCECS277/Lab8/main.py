'''10/12/22 Polymorphism Lab by Sebastian Rosas and Saiah Montoya

This program creates a game, where the user is a Hero and must fight 3 dragons to win. Every turn, you get the choice to attack one of the 3 dragons, but the dragon will return with an attack of their own. The goal is to do as much damage to each dragon before you run out of HP.
'''
import Dragon
import Hero
import FireDragon
import FlyingDragon
import check_input
import random

def main():
  '''Main menu'''
  name = input('What is your name, challenger?\n')
  player = Hero.Hero(name,50)
  dragons = [Dragon.Dragon('Boring Dragon',10),FireDragon.FireDragon('Fire Dragon',15,5),FlyingDragon.FlyingDragon('Flying Dragon',20,5)]
  
  print('\nWelcome to dragon training, ' + player.name, '\nYou must defeat 3 dragons')

  '''Gameplay loop. Player will attack with either their sword or arrows. After attacking, the player is attacked by a random dragon. Continues until player defeats all dragons or is defeated. '''
  while 0 == 0:
    print('\n'+str(player))
    for x in range(len(dragons)):
      print(str(x+1)+'. Attack '+str(dragons[x])+'\n')

    player_target = check_input.get_int_range('\nChoose a dragon to attack: ',1,len(dragons))
    player_attack = check_input.get_int_range('\nAttack with:\n1.Arrow (1D12)\n2.Sword (2D6)\nEnter Weapon: ',1,2)

    for x in range(len(dragons)):
      if player_target == x+1:
        if player_attack == 1:
          print(player.arrow_attack(dragons[x]))
        elif player_attack == 2:
          print(player.sword_attack(dragons[x]))

    random_dragon = random.randint(1,len(dragons))
    random_attack = random.randint(1,2)
    
    if random_attack == 1:
      print(dragons[random_dragon-1].basic_attack(player))
    elif random_attack ==2:
      print(dragons[random_dragon-1].special_attack(player))

    for dragon in dragons:
      if dragon.hp == 0:
        dragons.remove(dragon)

    if len(dragons) == 0:
      print('Congratulations! You defeated all three dragons. You passed the trial.')
      break
    if player.hp == 0:
      print('Uh oh. You died.')
      break
      
        
      
      
    


main()