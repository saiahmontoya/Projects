'''Program by Sebastian Rosas and Saiah Montoya 9/14/22 Group 13. This program challenges the user to guess the Capital City of a randomly generated State. Each time the user gets a question right, their score is incremented. The game finishes when the user decides they're done'''
import random

def read_file_to_dict():
  '''Opens text file and organizes the information into a dictionary, separating the State's and their Capitals'''
  with open('StateCapitals.txt') as file:
    
    StateCapitals_dict = {} 
    
    for line in file:
      list = []
      line_stripped = line.strip()
      list = line_stripped.split(',')
      StateCapitals_dict.update({list[0]:list[1]})

    return StateCapitals_dict

def get_random_state(states):
  '''Creates a list of all the States.'''
  StateCapitals_list = list(states.items())
  
  n = len(StateCapitals_list)
    
  randomState = StateCapitals_list[random.randint(0,n-1)]
  '''A random state is chosen and its' capital is stored''' 
  return randomState

def get_random_choices(states,correct_capital):
  incorrect_choices = 0
  states_list = list(states.values())
  n = len(states_list)
  possible_answers = [correct_capital]
  '''Randomly generates 3 random Capitals and puts them in a list with the correct
    choice'''
  while incorrect_choices != 3:
    choice = states_list[random.randint(0,n-1)]
    
    if choice not in possible_answers:
      possible_answers.append(choice)
      incorrect_choices += 1
  '''Randomizes the choices'''
  random.shuffle(possible_answers)
  return possible_answers



def ask_question(correct_state, possible_answers): 
  
  '''Asks question and prints possible answers'''

  answer_dict = {'A':0,'B':1,'C':2,'D':3}
  print('\nThe capital of', correct_state, 'is:')
  print('A:',possible_answers[0],'B:',possible_answers[1],'C:',possible_answers[2],'D:',possible_answers[3],'\n')
 
  while 0 == 0:
    user_answer = input('Enter selection: ')
    '''Only allows user to input A, B, C, or D'''
    if user_answer != 'A' and user_answer != 'B' and user_answer != 'C' and user_answer != 'D':
      print('print Invalid Input. Choose A, B, C, or D\n')
    else:
      break
  return answer_dict[user_answer]

def main():
  '''set variables'''
  states = read_file_to_dict()
  win_counter = 0
  
  print('-States Quiz-')
  '''Core of the program. Continues until you get 10 correct.'''
  for x in range(0,10):
    randomState = get_random_state(states)
    possible_answers = get_random_choices(states,randomState[1])
    user_answer = ask_question(randomState[0],possible_answers)
    '''Check answer to see if its correct. If correct the win counter will increase'''
    if possible_answers[user_answer] == randomState[1]:
      print('\nCorrect!\n')
      win_counter += 1
    else:
      print('\nIncorrect! Correct answer is',randomState[1])
  '''Displays the total score'''
  print('\nTotal Points:', win_counter)

main()