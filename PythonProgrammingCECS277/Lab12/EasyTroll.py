'''Easy Troll class from Entity superclass, object created in the beginner factory. '''
import Entity
import random
class EasyTroll(Entity.Entity):
  def __init__(self):
    super().__init__('Easy Troll',random.randint(4,5))

  def attack(self,entity):
    dmg = random.randint(1,5)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'