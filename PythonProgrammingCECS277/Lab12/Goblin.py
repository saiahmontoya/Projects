'''Hard Goblin class from Entity superclass, object created in the expert factory.'''
import Entity
import random
class Goblin(Entity.Entity):
  def __init__(self):
    super().__init__('Strong Goblin',random.randint(6,10))

  def attack(self,entity):
    dmg = random.randint(4,8)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'