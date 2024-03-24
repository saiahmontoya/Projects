'''Easy Ogre class from Entity superclass, object created in the beginner factory.'''
import Entity
import random
class EasyOgre(Entity.Entity):
  def __init__(self):
    super().__init__('Easy Ogre',random.randint(3,5))

  def attack(self,entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'