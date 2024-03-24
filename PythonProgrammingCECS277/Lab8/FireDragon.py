import Dragon
import random
'''Fire dragon is an object derived from the Dragon class that attacks using Fire. '''
class FireDragon(Dragon.Dragon):
  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, hero):
    damage = random.randint(5,9)
    if self.f_shots > 0:
      hero.take_damage(damage)
      self.f_shots -= 1
      return "The " +self.name+ " spews his fire, dealing " +str(damage)+ " damage!"
    else:
      return 'The ' +self.name+' failed their attack, dealing zero damage.'

  def __str__(self):
    return super().__str__()+'\nFire attacks remaining:' +str(self.f_shots)
  