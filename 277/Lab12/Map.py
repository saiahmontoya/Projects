'''Map Class, Creates the map of the dungeon maze, which is a 2D 5x5 grid map'''
class Map():
  _instance = None
  _initialized = False

  def __new__(cls):
    if cls._instance == None:
      cls._instance = super().__new__(cls)
    return cls._instance

  '''Creates 2D Map. Fills the list with False values, if values are not displayed it will show X'''
  def __init__(self):
    if not Map._initialized:
      self._revealed = [[False for x in range(5)]for x in range(5)]
      self._map = [[''for x in range(5)]for x in range(5)]
      Map._initialized = True

  def load_map(self,map_num):
    if map_num == 1:
      with open('map1.txt') as m:
        lines = m.readlines()
    if map_num == 2:
      with open('map2.txt') as m:
        lines = m.readlines()
    if map_num == 3:
    
      '''Open txt file'''
      with open('map3.txt') as m:
        lines = m.readlines()

    '''For X in 2D list it will change the map according to where the user is located'''
    for x in range(5):
      lines[x] = lines[x].strip() 
      counter = 0
      for character in lines[x]:
        self._map[x][counter] = character
        counter += 1
    self._revealed = [[False for x in range(5)]for x in range(5)]

  '''Returns the map in a string format showing the 5x5 grid'''
  def show_map(self,loc):
    for x in range(5):
      string = ''
      for y in range(5):
        if [x,y] == loc:
          string += '*  '
        elif self._revealed[x][y] == False:
          string += 'x  '
        else:
          string += self._map[x][y]
          string += '  '
      print(string)

  '''returns specified row in map'''
  def __getitem__(self,row):
    return self._map[row]

  '''REturns the number of rows in the map'''
  def __len__(self):
    return len(self._maps)

  '''Changes the location at which the hero is to True'''
  def reveal(self,loc):
    self._revealed[loc[0]][loc[1]] = True

  '''Overwrites the character in the map list at the specific spot with "n"'''
  def remove_at_loc(self,loc):
    self._map[loc[0]][loc[1]] = 'n'
        
        
    
  
  