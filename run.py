import random

print(""" 
Welcome HUMBLE USER , WE HOPE YOU WILL ENJOY THE ...!
""")
print(""" 
     _____  _  ____     _____  ____  ____     _____  ____  _____         
    /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/ 
      / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \ 
      | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   
      \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\ 


""")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
horizontal = 3
vertical = 3


def displayField():
  """ 
  A function that sets the field that iterates through,
  Sets the boundaries and core positions of the game
  """ 
  for x in range(horizontal):
    print('\n          +---+---+---+')
    print('          |', end='')
    for y in range(vertical):
      print('', field[x][y], end=' |')
  print('\n          +---+---+---+')


def inputInArray(num, turn):
  """ 
  Function that identifies the field against the players choice
  Used for both determining the winner function and running the game 
  """
  num -= 1
  if (num == 0):
    field[0][0] = turn
  elif (num == 1):
    field[0][1] = turn
  elif (num == 2):
    field[0][2] = turn
  elif (num == 3):
    field[1][0] = turn
  elif (num == 4):
    field[1][1] = turn
  elif (num == 5):
    field[1][2] = turn
  elif (num == 6):
    field[2][0] = turn
  elif (num == 7):
    field[2][1] = turn
  elif (num == 8):
    field[2][2] = turn


def checkWhoWon(field):
  # A function that indentifies the winner of the game Includes X Axis Y Axis and Horizontal
  
  # X Axis
  if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O'):
    print('\n   *** O has won!')
    return True
  elif (field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O'):
    print('\n   *** O has won!')
    return True
  elif (field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O'):
    print('\n   *** O has won!')
    return True

  # Y Axis
  elif (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O'):
    print('\n   *** O has won!')
    return True
  elif (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O'):
    print('\n   *** O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O'):
    print('\n   *** O has won!')
    return True
  # Cross  wins
  elif (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O'):
    print('\n   *** O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X'):
    print('\n   *** X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O'):
    print('\n  *** O has won!')
    return True


def main_function():
  """ 
  This is the main function that runs the game , Iterates/counts between the player turns,
  And determines the winner or a tie.
  """ 
  leaveLoop = False
  turn = 'X'
  turnCounter = 0
  choose = input(""" \n Do you wish to proceed? ... \n
  Or are you afrid the computer will best you! 
  \n    Choose yes or no : 
  """).lower()


  if (choose == 'yes' or choose == 'yea'):
    while (leaveLoop == False):
      if (checkWhoWon(field) == True): 
        displayField()
        break

      elif (turnCounter == 9 and checkWhoWon(field) != True): # Sets the tie if there is no winner after turn 9 
        print(""" 
                   ~~ This is a tie! ~~ 
            _____  _  ____     _____  ____  ____     _____  ____  _____         
           /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/ 
             / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \ 
             | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   
             \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\ 

        """ ) 
        break

     ### Players turn
      elif (turnCounter % 2 == 1): # Determines cpu goes first 
        displayField()
        chosenNumber = int(input('\nPlease chose a number between 1 and 9 : '))
        if (chosenNumber >= 1 and chosenNumber <= 9 and chosenNumber != aiChoice): #Makes sure player can not pick the number already picked by CPU,This game me a headache but was such a simple solution
          inputInArray(chosenNumber, 'X')
          numbers.remove(chosenNumber)
          turnCounter += 1
        else:
          print('Invalid input number, Please try again , Numbers 1 - 9 ONLY!\n************DO NOT copy already used numbers :) ')

     ### Competitors / Ai turn
      else:
        while (True):
          aiChoice = random.choice(numbers)
          print('\n Computer has chosen: ', aiChoice)
          if (aiChoice in numbers):
            inputInArray(aiChoice, 'O')
            numbers.remove(aiChoice)
            turnCounter += 1
            break
  
  else:
    print('***** Better luck next time gamer :) ******')
  
  
main_function()

