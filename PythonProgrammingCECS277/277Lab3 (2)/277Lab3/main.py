'''Group 13 - Saiah Montoya and Sebastian Rosas'''
'''This program displays a customizable minesweeper grid with a certain number of rows, columns, and bombs, based on the user's input.'''
import check_input
import random


def place_mines(mines,grid,rows,columns):
  
  mines_placed = 0
  
  while mines_placed != mines:
    row = random.randint(0,rows-1)
    column = random.randint(0,columns-1)
    '''Takes the number of bombs and randomly assigns them to different locations'''
    if grid[row][column] != 'X':
      grid[row][column] = 'X'
      mines_placed +=1

  return grid
     
  
def display_board(grid,rows,columns):
  '''Creating the nested list'''
  for x in grid:
    list = []
    list = x
    counter = 0
    for y in list:
      print(y,end='')
      counter += 1
      if counter == columns:
        print()
        
def count_mines(grid):
  i = 0
  j = 0
  row = 0
  column = 0  
  row_length = len(grid)
  column_length = len(grid[0])
  '''Takes the lengths of the row and column and checks if there are bombs in each position.'''
  for i in range(0, row_length):    
    for j in range(0, column_length):      
      if grid[i][j] == 'X':        
        continue          
      mine_count = 0
      '''checks the surrounding values in the list. If the value is next to a bomb, it           adds 1  '''
      for row in range(i - 1, i + 2):        
        if (row >= 0) and (row <= row_length - 1):          
          for column in range(j - 1, j + 2):            
            if (column >= 0) and (column <= column_length - 1):              
              if grid[row][column] == 'X':                
                mine_count += 1     
      '''Updates grid'''
      grid[i][j] = mine_count
            
        

def main_func():

  '''Takes the user input and applies it to the rows, columns and mines'''  
  rows = check_input.get_int_range('How many rows? (5-10) ',5,10)
  columns = check_input.get_int_range('How man columns? (5-10) ',5,10)
  mines = check_input.get_int_range('How many mines? (5-10) ',5,10)
  
  '''Creates a grid using nested lists'''
  grid = [[0 for x in range(columns)] for y in range(rows)]

  
  print(grid)  
  grid = place_mines(mines,grid,rows,columns)
  count_mines(grid)
  display_board(grid,rows,columns)

main_func()
