def getHitProbability(R, C, G):
  # Write your code here
  gSize = R * C
  battleShips = 0
  for r in range(R):
    for c in range(C):
      if G[r][c] == 1:
        battleShips += 1
  hitProb = float(battleShips / gSize)
  return hitProb

Rows = 2
Columns = 3
Grid = [[0, 0, 1],[1, 0, 1]]
print getHitProbability(Rows, Columns, Grid) 
