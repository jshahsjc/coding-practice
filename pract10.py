"""
https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/

Split an array into two equal Sum subarrays
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
Asked In : Facebook interview

"""
import heapq

class Playlist:
    """
    class to play with lists.
    """
    def __init__(self, inList):
        self.inList = inList

    def __str__(self):
        return f"In List: {self.inList}."

    def equalSumSplit(self):
        sum  = 0
        temp = 0
        for n in self.inList:
            sum += n
        for i,n in enumerate(self.inList):
            temp += n
            sum -= n
            if temp == sum:
                return (self.inList[:i+1], self.inList[i+1:])
        return 0

    def findNLargest(self, n):
        return heapq.nlargest(n, self.inList)[-1]

'''
x = Playlist([4,1,2,3])
print(f'playlist is: {x}')
print(x.equalSumSplit())
print(x.findNLargest(2))
'''
