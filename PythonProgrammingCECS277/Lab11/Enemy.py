'''Enemy Class, extension of Entity, Creates the monsters that the hero will encounter on his journey'''

import Entity
import random

class Enemy(Entity.Entity):
  '''Enemy is either an Imp, Slime, Skeletom, Ogre, or Golem'''
  def __init__(self):
    names = ['Imp','Slime','Skeleton','Ogre','Golem']
    super().__init__(names[random.randint(0,4)],random.randint(4,8))

  '''Attacks from enemys will do damage from 1-4'''
  def attack(self,entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return self.name+' attacks you for '+str(dmg)+' damage!'