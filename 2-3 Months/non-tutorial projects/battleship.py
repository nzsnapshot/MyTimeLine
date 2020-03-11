import random

boat_lengths = [2,3,4,5]
game_board = [0 for x in range(0,100)]

for boat_len in boat_lengths:
    position_found = False
    vertical = random.randint(0,1)

    if vertical == 0:
        while not position_found:
            test_position = random.randint(0,99)
            position_found = True
            if len(game_board) <= test_position+boat_len:
                position_found = False
            else:
                for i in range(0,boat_len):
                    if game_board[test_position+i] != 0:
                        position_found = False
                    if test_position%10+i >= 10:
                        position_found = False
        for z in range(0,boat_len):
            game_board[test_position+z] = boat_len

    elif vertical == 1:
        while not position_found:
            test_position = random.randint(0,99)
            position_found = True
            if len(game_board) <= test_position+boat_len*10:
                position_found = False
            else:
                for i in range(0,boat_len):
                    if game_board[test_position+i*10] != 0:
                        position_found = False
                    if test_position+i*10 >= 100:
                        position_found = False
        for z in range(0,boat_len):
            game_board[test_position+z*10] = boat_len

with open('battleship board.txt', 'w') as map_file:
    for y in range(0,10):
        for x in range(0,10):
            map_file.write(str(game_board[x+y*10]))
        map_file.write('\n')


#------boat coordinates for testing-------
#e.g. (vertical,horizontal)
#Destroyer(2hits) = (1,1) and (1,2)
#Cruiser(3hits) = (7,2),(7,3), and (7,4)
#Battleship(4hits) = (0,6),(0,7),(0,8), and (0,9)
#Carrier(5hits) = (2,6),(3,6)(4,6)(5,6), and (6,6)

# ----------functions--------------------------------
def drawBoard(gB):
  # this function receives a list of lists
  # the list of lists must be a 10x10 structure
  # it then uses this to draw an index row and column
  # and the board itself...
  print('----------------------------------------------')
  print('    0 1 2 3 4 5 6 7 8 9')
  for i in range(0, 10, 1):
    print(i, ' ', end='')
    for j in range(0, 10, 1):
      s = ' ' + str(gB[i][j])
      print(s, end='')
    print()
  print('----------------------------------------------')
  return

# -----------background setup (preparing data)-------
# 1 import map data
# open the board file for reading
inFile = open('battleship board.txt', 'r')
map = []  # a list of lists
for templine in inFile:
  newtempline = templine.strip('\n')
  templist = list(newtempline)
  map.append(templist)

# must convert these strings to ints
for x in range(0, 10, 1):
  for y in range(0, 10, 1):
    map[x][y] = int(map[x][y])

gameboard = []
for i in range(0, 10, 1):
  gameboard.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
drawBoard(gameboard)

# ----------startup conditions for game--------------
notAllHit = True
destroyer = 0  # 2
cruiser = 0  # 3
battleship = 0  # 4
carrier = 0  # 5
destroyerCheck = True
cruiserCheck = True
battleshipCheck = True
carrierCheck = True
# -------------the game------------------------------
while notAllHit:
    print('----------------------------------------------')
    row = int(input('Enter a vertical integer to fire at (0-9):'))
    column = int(input('Enter a horizontal integer to fire at(0-9):'))
    ############# Below is the try and except statements.
    ############# try and except allows you to handle errors and give a different outcome
    ############# This way the user does not get interrupted or the programme stops
    try:    
        if gameboard[row][column] == 'X' or gameboard[row][column] == '.':
          print('You already fired at these coordinates, try again.')
          print('----------------------------------------------')
        else:
          if map[row][column] == 0:
            print('MISS')
            gameboard[row][column] = '.'
            drawBoard(gameboard)
          else:
            print('HIT')
            gameboard[row][column] = 'X'
            hitBoatType = map[row][column]
            #map[row][column] = 0
            drawBoard(gameboard)

          if map[row][column] == 2:
            destroyer += 1
            if destroyer == 2:
              if destroyerCheck == True:
                print('You sunk the Destroyer!')
                destroyerCheck = False

          if map[row][column] == 3:
            cruiser += 1
            if cruiser == 3:
              if cruiserCheck == True:
                print('You sunk the Cruiser!')
                cruiserCheck = False

          if map[row][column] == 4:
            battleship += 1
            if battleship == 4:
              if battleshipCheck == True:
                print('You sunk the Battleship!')
                battleshipCheck = False

          if map[row][column] == 5:
            carrier += 1
            if carrier == 5:
              if carrierCheck == True:
                print('You sunk the Carrier!')
                carrierCheck = False
    except IndexError:
        error = print('Please enter a valid input between 0-9:')

    if destroyerCheck == False and cruiserCheck == False and battleshipCheck == False and carrierCheck == False:
        notAllHit = False

print('All boats sunk.')
print('You Win!')