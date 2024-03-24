from random import randint
import check_input

'''Program by Saiah Montoya and Sebastian Rosas'''

'''Choose Rock Paper or Scissors!'''
def weapon_menu():
  while 0 == 0:
    weapon = {"R":"Rock", "P":"Paper", "S":"Scissors", "B":"Back"}
    print("\nChoose your weapon:")
    try:
      player = weapon[input("R. Rock\nP. Paper\nS. Scissors?\nB. Back\n ")]
      return player
    except KeyError:
      print("\nInvalid Input use 'R', 'P', 'S', or 'B'\n" )
'''Rejects Invalid inputs'''

    
'''Assigns random choice for Computer'''
def comp_weapon():
  t = ["Rock", "Paper", "Scissors"]
  computer = t[randint(0, 2)]
  return computer

'''Main Menu'''
def start_menu():
  print("RPS Menu")
  print("1. Play Game")
  print("2. Show Score")
  print("3. Quit\n")
  player = check_input.get_int_range("Enter 1, 2, or 3:\n",1,3)
  return player

'''Find the winner between Player or Computer. Checks inputs and compares them. '''
def find_winner(player, computer):
  if player == computer:
    print("Tie!")
    return 0
  elif player == "Rock":
    if computer == "Paper": 
      print()
      print(f"You lose. {computer} covers {player.title()}.")
      return 2
      print()
    else:
      print()
      print(f"You win! {player.title()} smashes {computer}.")
      return 1
      print()
  elif player.title() == "Paper":
    if computer == "Scissors":
      print()
      print(f"You lose. {computer} cuts {player.title()}.")
      return 2
      pass
      print()
    else:
      print()
      print(f"You win!, {player.title()} covers {computer}.")
      return 1
      pass
      print()
  elif player.title() == "Scissors":
    if computer == "Rock":
      print()
      print(f"You lose. {computer} smashes {player.title()}.")
      return 2
      pass
      print()
    else:
      print()
      print(f"You win! {player.title()} cuts {computer}.")
      return 1
      pass
      print()  
      
'''Display scores from player and computer'''      
def display_scores(player, computer):
  print("Your score is\n Player = ",player,"\n", "Computer = ", computer)
  
'''Main function that houses and drives the program'''
def main_func():
  playerScore = 0
  compScore = 0
  
  while 0==0:
    player = start_menu()
    
    if player == 1:
      while 0 == 0:
        player_weapon = weapon_menu()
        computer_weapon = comp_weapon()
        
    
        
        if player_weapon == "Back":
          break 

        results = find_winner(player_weapon,computer_weapon)
        if results == 1:
          playerScore += 1
        if results == 2:
          compScore +=1
          
    if player == 2:
       display_scores(playerScore,compScore)
      
    if player == 3:
      print('Final Score \n')
      display_scores(playerScore, compScore)
      break

main_func()

