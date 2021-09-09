"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

def mergeIntervals(ivls):
    res = []
    res.append(ivls[0])
    for i in range(1, len(ivls)):
        if ivls[i][0] < res[-1][1]:
            res[-1][1] = ivls[i][1]
        else:
            res.append(ivls[i])
    return res














def mergeIntervals(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
    i = 0
    j = 1
    output = []
    if len(intervals) <= 1:
        return intervals

    while j < len(intervals):
        if intervals[j][0] <= intervals[i][1]:
            output.append([intervals[i][0], intervals[j][1]])
            j += 1
        else:
            output.append(intervals[j])
            i = j
            j += 1

    return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))

intervals = [[1,4],[4,5]]
print(mergeIntervals(intervals))



def mergeIntervals(nums):
    nums = sorted( nums, key  = lambda x: x[0] )
    j = 1
    while j < len(nums):
        if nums[j][0] <= nums[j - 1][1]:
            nums[j - 1][1] = nums[j][1]
            del nums[j]
        j += 1
    return nums
