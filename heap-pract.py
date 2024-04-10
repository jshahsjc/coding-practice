"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.


"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while stones:
            s1 = -heapq.heappop(stones)
            if not stones:
                return s1
            s2 = -heapq.heappop(stones)
            if s1 > s2:
                heapq.heappush(stones, s2 - s1)
        return 0
