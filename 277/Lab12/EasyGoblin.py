'''Easy Goblin class from Entity superclass, object created in the beginner factory.'''
import Entity
import random
class EasyGoblin(Entity.Entity):
  def __init__(self):
    super().__init__('Easy Goblin',random.randint(3,4))

  def attack(self,entity):
    dmg = random.randint(1,3)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'
