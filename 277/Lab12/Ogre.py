'''Hard Ogre class from Entity superclass, object created in the expert factory'''
import Entity
import random
class Ogre(Entity.Entity):
  def __init__(self):
    super().__init__('Strong Ogre',random.randint(6,12))

  def attack(self,entity):
    dmg = random.randint(6,10)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'