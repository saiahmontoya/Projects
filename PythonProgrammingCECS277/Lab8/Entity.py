'''Entity class creates all the other objects' attributes. Name, HP, Max Hp are derived from here, but each has a unique name, hp, etc. based on their own respective attributes.''' 
class Entity:
  def __init__(self, name='', hp=0):
    self.name = name
    self.hp = hp
    self.max_hp = self.hp 
  def __str__(self):
    return self.name + ":" + str(self.hp) + "/"+ str(self.max_hp)

  def take_damage(self,damage):
    self.hp -= damage
    if self.hp < 0:
      self.hp = 0

  @property
  def get_name(self,name):
    return name

  @property
  def get_hp(self,hp):
    return hp
    

  