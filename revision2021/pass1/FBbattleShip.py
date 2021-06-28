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


def findBattleship(N):
    # Take two indices, one for rows, one for columns
    battleShip =  []
    for x in range(N):
        for y in range(N):
            # Two for loops = O(n^2)
            # Carrying on for now
            if bomb_location(x, y):
                battleShip.append((x, y))
            # Think where to bomb next
            # Case1: ship is horizontally placed
            if (x - 2) >= 0 and (x + 2) <= N:
                if bomb_location(x - 1, y) && bomb_location(x - 2, y):
                    battleShip.append((x - 1, y), (x - 2, y))
                if bomb_location(x + 1, y) && bomb_location(x + 2, y):
                    battleShip.append((x + 1, y), (x + 2, y))
            elif (x - 1) >= 0:
                if bomb_location(x - 1, y) && bomb_location(x + 1, y):
                    battleShip.append((x - 1, y), (x + 1, y))
            ## More cases can be added to optimize this further.
            ## Need to do more thinking.
            else:
                pass

            # Case2: ship is vertically placed
            if (y - 2) >= 0:
                if bomb_location(x, y - 1) && bomb_location(x, y - 2):
                    battleShip.append((x, y - 1), (x, y - 2))
            elif (y + 2) <= N:
                if bomb_location(x, y + 1) && bomb_location(x, y + 2):
                    battleShip.append((x, y + 1), (x, y + 2))
            else:
                pass
