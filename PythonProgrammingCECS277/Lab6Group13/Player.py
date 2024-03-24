import Die

class player:
  '''Player class controls the dice game. Start with 0 points and increase based on the dice rolls you get.
  The dice data is stored in a list and is arranged in order of least to greatest. When the dice outputs the data it is compared and points are added based on results.'''
  def __init__(self):
    player.points = 0
    player.dices = [Die.Die(),Die.Die(),Die.Die()]

  def get_points(self):
    return self.points

  def roll_dice(self):
    '''temporary list to store sorted dices'''
    list = []
    
    for dice in self.dices:
      dice.roll()

    '''these if statements sort the dices into order from smallest to largests values'''
    if self.dices[0] < self.dices[1]:
      if self.dices[1] < self.dices[2]:
        list.append(self.dices[0])
        list.append(self.dices[1])
        list.append(self.dices[2])
      
      elif self.dices[0] < self.dices[2]:
        list.append(self.dices[0])
        list.append(self.dices[2])
        list.append(self.dices[1])

      else:
        list.append(self.dices[2])
        list.append(self.dices[0])
        list.append(self.dices[1])

    elif self.dices[1] < self.dices[0]:
      if self.dices[0] < self.dices[2]:
        list.append(self.dices[1])
        list.append(self.dices[0])
        list.append(self.dices[2])
      
      elif self.dices[1] < self.dices[2]:
        list.append(self.dices[1])
        list.append(self.dices[2])
        list.append(self.dices[0])

      else:
        list.append(self.dices[2])
        list.append(self.dices[1])
        list.append(self.dices[0])

    elif self.dices[1] == self.dices[0]:
      if self.dices[0] < self.dices[2]:
        list.append(self.dices[0])
        list.append(self.dices[1])
        list.append(self.dices[2])
      else:
        list.append(self.dices[2])
        list.append(self.dices[1])
        list.append(self.dices[0]) 

      '''sets sorted list to be the new list of dices'''
    self.dices = list

  '''Functions are uesd to add compare results and add points'''
  def has_pair(self):
    
    if self.dices[0] == self.dices[1] and self.dices[0] != self.dices[2]:  
      self.points += 1
      return True
      
    elif self.dices[1] == self.dices[2] and self.dices[2] != self.dices[0]:
      self.points += 1
      return True
    
  def has_3_of_a_kind(self): 
    
    if self.dices[0] == self.dices[1] and self. dices[0] == self.dices[2]:
      self.points += 3
      return True

  def has_series(self):
    
    if self.dices[2] - self.dices[1] == 1 and self.dices[1] - self.dices[0] == 1:
      self.points += 2
      return True

  def __str__(self):
    
    return '\nD1 = '+str(self.dices[0])+', D2 = '+str(self.dices[1])+', D3 = '+str(self.dices[2])+'\n'
    