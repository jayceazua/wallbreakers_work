# 
# Consider a square grid of size N, where N >= 3. I have placed a battleship of 
# size 3 somwhere in the grid, and you want to sink my battleship by ordering 
# the bombing of specified coordinates. 
# 
# The battleship can only be placed vertically or horizontally, not diagonally. 
# Every coordinate which does not contain the battleship is empty. Your task is 
# to write a function which takes as input N, and returns the 3 coordinates of 
# the battleship. 
# 
# Assume you have a function, boolean bomb_location(x, y), which will return 
# True if (x, y) "hits" the battleship and False if (x, y) misses the
# battleship. 
# 
# For example - in the following grid your function find_battleship(grid_size), 
# given grid_size of 8, would return ((2, 1), (2, 2), (2, 3)):
# 
# . . . . . . . .
# . . X . . . . .
# . . X . . . . .
# . . X . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# 



def find_battleship(grid_size):
  coordinates = []
  # brute force solution 
  for x in range(grid_size): # O(n^2)
    for y in range(grid_size):
      if bomb_location(x, y):
        coordinates.append((x, y))
        # no point in going left or up since I already went from the upper left corner...
        # move down
        if (x != grid_size - 2) and bomb_location(x, y+1):
          coordinates.append((x, y+1))
          coordinates.append((x, y+2))
        # move right
        if (y != grid_size - 2) and bomb_location(x+1, y):
          coordinates.append((x+1, y))
          coordinates.append((x+2, y))
        return tuple(coordinates)

def bomb_location(x, y):
  # stores user bombing into a tuple
  shelling = (x, y)
  # ship's location is store as a set
  ship_location = {(2, 1), (2, 2), (2, 3)}
  if shelling in ship_location:
    return True
  return False

if __name__ == "__main__":
  grid = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
  ]

  grid_size = len(grid)
  ship_size = 3

  print(find_battleship(grid_size))

  

  
