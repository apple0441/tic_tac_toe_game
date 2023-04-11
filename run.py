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
    print('\n+---+---+---+')
    print('|', end='')
    for y in range(vertical):
      print('', field[x][y], end=' |')
  print('\n+---+---+---+')

