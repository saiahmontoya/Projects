'''The hero class, AKA the player. Extended from Entity class.'''
import Entity
import random
import Map

class Hero(Entity.Entity):
  '''initializes the name and HP of the Hero'''
  def __init__(self,name):
    super().__init__(name,25)
    self._loc = [0,0]

  @property
  def loc(self):
    return self._loc
    
  '''Attack deals random damage from 2 to 5'''
  def attack(self,entity):
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    return 'You slash at the '+entity.name+' with you sword for '+str(dmg)+' damage!'

  '''Go_Direction functions change the map by updating the Hero's location by adding/subtracting 1 from the column or row on the map. It will return X if the location is out of bounds'''
  
  '''Move hero up'''
  def go_north(self):
    if self.loc[0] == 0:
      return 'X'
    else:
      self._loc[0] -= 1
      m = Map.Map()
      return m[self.loc[0]][self.loc[1]]

  '''Move hero down'''
  def go_south(self):
    if self.loc[0] == 4:
      return 'X'
    else:
      self._loc[0] += 1
      m = Map.Map()
      return m[self.loc[0]][self.loc[1]]

  '''Moves hero left'''
  def go_west(self):
    if self.loc[1] == 0:
      return 'X'
    else:
      self._loc[1] -= 1
      m = Map.Map()
      return m[self.loc[0]][self.loc[1]]

  '''Move hero right'''
  def go_east(self):
    if self.loc[1] == 4:
      return 'X'
    else:
      self._loc[1] += 1
      m = Map.Map()
      return m[self.loc[0]][self.loc[1]]