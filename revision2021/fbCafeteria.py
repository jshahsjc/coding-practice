"""
A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right remain empty.
There are currently MM diners seated at the table, the iith of whom is in seat S_iS
i
​	 . No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
Constraints
1 \le N \le 10^{15}1≤N≤10
15

1 \le K \le N1≤K≤N
1 \le M \le 500,0001≤M≤500,000
1 \le S_i \le N1≤S
i
​	 ≤N
Sample Test Case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3
Sample Test Case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1
Sample Explanation
In the first case, the cafeteria table has N = 10N=10 seats, with two diners currently at seats 22 and 66 respectively. The table initially looks as follows, with brackets covering the K = 1K=1 seat to the left and right of each existing diner that may not be taken.
  1 2 3 4 5 6 7 8 9 10
  [   ]   [   ]
Three additional diners may sit at seats 44, 88, and 1010 without violating the social distancing guidelines.
In the second case, only 11 additional diner is able to join the table, by sitting in any of the first 33 seats.
"""

def getMaxNewDiners(TableSize, distance, dinerSeated, takenSeats):
    # get blocked seats:
    blockedSeats = []
    for seat in takenSeats:
        if (seat - distance) >= 1:
            blockedSeats.append((seat - distance))
        if (seat + distance) <= TableSize:
            blockedSeats.append((seat + distance))
    # now we have 2 lists to work with;
    # takenSeats and blockedSeats, put them together as blocked
    blockedSeats += takenSeats
    # now get the remaining seats.
    openSeats = []
    for n in range( 1, TableSize+1 ):
        if n not in blockedSeats:
            openSeats.append(n)
    # iterate through open seats and check for distance
    availableSeats = 0
    for o in openSeats:
        leftBlock = o - distance
        rightBlock = o + distance
        cantUse = False
        for s in range(leftBlock, rightBlock + 1):
            if s in takenSeats:
                cantUse = True
            else:
                pass
        if not cantUse:
            availableSeats += 1
    return availableSeats

print getMaxNewDiners(10, 1, 2, [2, 6])
