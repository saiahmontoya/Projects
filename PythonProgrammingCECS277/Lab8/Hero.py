import Entity
import random
'''Hero class is the player. The hero has two attacks, the sword attack and arrow attack. The damage of each is random based on the respective ranges given. The hero must deal more damage than recieved or else they will lose. '''
class Hero(Entity.Entity):
  
  def sword_attack(self,dragon):
    damage = random.randint(1,6) + random.randint(1,6)
    dragon.take_damage(damage)

    return '\nYou attack the '+dragon.name+' with your sword for '+str(damage)+' damage.'
    
  def arrow_attack(self,dragon):
    damage = random.randint(1,12)
    dragon.take_damage(damage)

    return '\nYou hit the '+dragon.name+' with an arrow for '+str(damage)+' damage.'