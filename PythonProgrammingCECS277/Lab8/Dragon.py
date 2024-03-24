import Entity
import random
'''Dragon class creates an entity named Dragon with a basic attack and special attack. This dragon class is the foundation for the other dragon objects. Attack does random damage between 3 - 7. Special attack does random damage from 4-8'''
class Dragon(Entity.Entity):
  
  def basic_attack(self,hero):
    damage = random.randint(3,7)
    hero.take_damage(damage)
    return 'The '+self.name+' attacks you with its tail for '+str(damage)+' damage.'

  def special_attack(self,hero):
    damage = random.randint(4,8)
    hero.take_damage(damage)
    return'The '+self.name+' slashes you with its claws for '+str(damage)+' damage.'
