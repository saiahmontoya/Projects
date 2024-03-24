'''Expert Factory from Abstract Factory. Class creates a random Strong Enemy, either a Goblin, Ogre, or Troll'''
import EnemyFactory
import Troll
import Ogre
import Goblin
import random
class ExpertFactory(EnemyFactory.EnemyFactory):
  def create_random_enemy(self):
    type = random.randint(1,3)
    if type == 1:
      return Goblin.Goblin()
    if type == 2: 
      return Ogre.Ogre()
    if type == 3:
      return Troll.Troll()