"""
https://leetcode.com/problems/intersection-of-three-sorted-arrays/solution/
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.



Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []


Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

def intersectThree(a1, a2, a3):
    i = j = k = 0
    res = []
    keep = [a1, a2, a3]
    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] == a2[j] == a3[k]:
            res.append(a1[i])
        else:
            if a1[i] < a2[j]:
                i += 1
            elif a2[j] < a3[k]:
                j += 1
            else:
                k += 1

    return res
