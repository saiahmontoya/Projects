import Dragon
import random
'''Flying dragon is derived from the Dragon class. This dragon has flying attack.'''
class FlyingDragon(Dragon.Dragon):
  def __init__(self,name,max_hp,swoops):
    super().__init__(name,max_hp)
    self.swoops = swoops

  def special_attack(self,hero):
    if self.swoops > 0:
      damage = random.randint(5,8)
      hero.take_damage(damage)
      self.swoops -= 1
      return 'The '+self.name+' swoops down on you for '+str(damage)+' damage.'
    else:
      return 'The '+self.name+' tried to swoop but failed. You take no damage.'

  def __str__(self):
    return super().__str__()+'\nSwoop attacks remaining: '+str(self.swoops)
    