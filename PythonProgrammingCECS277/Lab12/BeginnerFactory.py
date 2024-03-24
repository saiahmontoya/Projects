'''Beginner Factory randomly creates easy enemies, either easy goblin, easy ogre, or eay troll'''
import EnemyFactory
import EasyGoblin
import EasyOgre
import EasyTroll
import random
class BeginnerFactory(EnemyFactory.EnemyFactory):
 def create_random_enemy(self):
  type = random.randint(1,3)
  if type == 1:
     return EasyGoblin.EasyGoblin()
  if type == 2:
    return EasyOgre.EasyOgre()
  if type ==3:
    return EasyTroll.EasyTroll()