'''Entity Abstract Class, Creates the character's attributes like HP and Name, and creates the functions to heal, damage, or take damage.'''
import abc

class Entity:
  def __init__(self,name,max_hp):
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def hp(self):
    return self._hp

  @property
  def name(self):
    return self._name

  def take_damage(self,dmg):
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    return self.name+'\nHP: '+str(self.hp)+'/'+str(self._max_hp)

  def heal(self):
    self._hp = self._max_hp

  @abc.abstractmethod
  def attack(self,entity):
    pass