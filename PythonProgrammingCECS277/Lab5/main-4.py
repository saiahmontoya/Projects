'''Group 13 Saiah Montoya and Sebastian Rosas. This program creates a 20x20 grid that allows the user to create a rectangle using their own height and width dimensions. It takes the user's input within 1-5, and displays the rectangle within the grid. The user is given the option to move the rectangle up, down, left, or right.'''
import rectangle
import check_input

'''Prints 20 x 20 grid'''
def display_grid(grid):
  for y in grid:
    print()
    for x in y:
      print(x,'  ',end='')

'''Clears the grid and removes all rectangle properties'''
def reset_grid(grid):
  grid = [['.' for x in range(20)] for x in range(20)]
  return grid

'''Places rectangle using rectangle hieght and width properties'''  
def place_rect(grid,rect):
  for y in range(rect.y,rect.height+rect.y):
    for x in range(rect.x,rect.width+rect.x):
      grid[y][x] = '*'
  return grid
  


def main():
  
  '''takes the user's input for height and width'''
  width = int(check_input.get_int_range("Enter Rectangle Width (1-5): ",1,5))
  height = int(check_input.get_int_range("Enter Rectange Height (1-5): ",1,5))
  
  '''create nested list for grid'''
  grid= []
  grid = reset_grid(grid)
  user_rectangle = rectangle.Rectangle(width,height)
  

  '''loop to store menu'''
  while 0 == 0:

    '''Call functions'''
    grid = reset_grid(grid)
    grid = place_rect(grid,user_rectangle)
    display_grid(grid)
    
    '''Option menu'''
    print('\n\n1. Move Rectangle Up')
    print('2. Move Rectangle Down')
    print('3. Move Rectangle Left')
    print('4. Move Retangle Right')
    print('5. Quit')

    user_input = check_input.get_int_range('Enter a number 1-5: ',1,5)
    
    
    '''Takes user input and applies it to the movement of the rectangle'''
    if user_input == 5:
      break
      
    elif user_input == 1:
      if user_rectangle.y == 0:
        print('\nYou have reached the border. Try again')
      else:
        user_rectangle.move_up()
        
    elif user_input == 2:
      if user_rectangle.y == 20 - user_rectangle.height:
        print('\nYou have reached the border. Try again')
      else:
        user_rectangle.move_down()
      
    elif user_input == 3:
      if user_rectangle.x == 0:
        print('\nYou have reacehd the border. Try again')
      else:
        user_rectangle.move_left()

    elif user_input == 4:
      if user_rectangle.x == 20 - user_rectangle.width:
        print('\nYou have reached the border. Try again')
      else:
        user_rectangle.move_right()

  
main()