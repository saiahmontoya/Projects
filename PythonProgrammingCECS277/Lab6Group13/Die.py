import random


class Die:
  '''Creates dice class. Create dice object by establishing 6 sides.
  Rolling the dice generates a random number for each of the dice. 
  Each of the attributes allow the dice to compare to one another.'''

  def __init__(self,sides=6):
    self.sides = sides
    self.value = 0

  def roll(self):
    self.value = random.randint(1,self.sides)
    return self.value

  def __str__(self):
    return str(self.value)

  def __lt__(self,other):
    if  self.value < other.value:
      return True

  def __eq__(self,other):
    if self.value == other.value:
      return True

  def __sub__(self,other):
    return self.value - other.value

