"""
LC 986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

Input:
firstList = [[0,5],[5,10],[13,23],[24,25]],
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output:
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]

Constraints:

    0 <= firstList.length, secondList.length <= 1000
    firstList.length + secondList.length >= 1
    0 <= starti < endi <= 10^9
    endi < starti+1
    0 <= startj < endj <= 10^9
    endj < startj+1

"""

def intervalIntersect(fl, sl):
    i = j = 0
    res = []
    if len(fl) == 0 or len(sl) == 0:
        return []

    while i < len(fl) and j < len(sl):
        left_edge = max(fl[i][0], sl[j][0])
        right_edge = min(fl[i][1], sl[j][1])
        if left_edge <= right_edge:
            res.append((left_edge, right_edge))

        if fl[i][1] <= sl[j][1]:
            i += 1
        else:
            j += 1
    return res
