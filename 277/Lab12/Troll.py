'''Hard Troll class from Entity superclass, object created in the expert factory. '''
import Entity
import random
class Troll(Entity.Entity):
  def __init__(self):
    super().__init__('Strong Troll',random.randint(10,14))

  def attack(self,entity):
    dmg = random.randint(8,12)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'