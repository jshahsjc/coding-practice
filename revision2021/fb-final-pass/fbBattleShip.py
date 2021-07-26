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

def battleship(N):
    res = ()
    for x in range(N):
        for y in range(N):
            if bomb_location(x, y):
                res.append((x, y))
                if x + 2 <= N and bomb_location(x + 1, y):
                    res.append((x + 1, y), (x + 2, y))
                    break
                if y + 2 <= N and bomb_location(x, y + 1):
                    res.append((x, y + 1), (x, y + 2))
                    break

    return res
