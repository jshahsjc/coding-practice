# Consider a square grid of size N, where N >= 3. I have placed a battleship of
# size 3 somewhere in the grid, and you want to sink my battleship by ordering
# the bombing of specified coordinates.

# The battleship can only be placed vertically or horizontally, not diagonally.
# Every coordinate which does not contain the battleship is empty. Your task
# is to write a function which takes as input N, and returns the 3 coordinates of
# the battleship.

# Assume you have a function, boolean bomb_location(x, y), which will return
# True if (x, y) 'hits' the battleship and False if (x, y) misses the battleship.

# For example - in the following grid your function find_battleship(grid_size),
# given gride_size of 8, wourd return ((2,1), (2,2), (2,3))

def bomb_location(bomb_order):
   ship_location = ((2,1), (2,2), (2,3))
   return bomb_order in ship_location

def find_battleship(n):
   res = []
   for i in range(n):
      for j in range(n):
         if bomb_location((i, j)):
            res.append((i, j))
            if (i + 2) <= n \
               and bomb_location((i + 1, j)) \
               and bomb_location((i + 2, j)):
               res.append((i + 1, j))
               res.append((i + 2, j))
               return res
            elif (j + 2) <= n \
               and bomb_location((i, j + 1)) \
               and bomb_location((i, j + 2)):
               res.append((i, j + 1))
               res.append((i, j + 2))
               return res
            else:
               pass
   return res

print find_battleship(100)
