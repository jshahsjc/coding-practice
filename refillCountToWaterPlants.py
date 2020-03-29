"""
watering plants - Google OA:
https://leetcode.com/discuss/interview-question/394347/
"""

"""
Approach:
   first find howmany times the left and right pointers (water can) will move.
   In this case, it will be number of plants, divide by 2.

   Initialize 2 variables, each with water can capacities.
   Initialize refill variable to 2 (since both cans refill once at the beginning), to keep track of total refills of both cans.
   Upon each hop, incremet refill count if needed.

"""

def refillCountToWaterPlants(plants, cap1, cap2):
   hops = len(plants) // 2
   refill = 2
   can1 = cap1
   can2 = cap2

   for k in range(hops):
      if can1 < plants[k]:
         refill += 1
         can1 = cap1
      can1 -= plants[k]

      if can2 < plants[-(k+1)]:
         refill += 1
         can2 = cap2
      can2 -= plants[-(k+1)]

   return refill

P = [2, 4, 5, 1, 2]
c1, c2 = 5, 7

print "total refill needed: " + str(refillCountToWaterPlants(P, c1, c2))
