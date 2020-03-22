"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

"""
This is a search problem.
Linear brute force O(n):
for each version in the version list:
   check isBadVersion(version) if True, return version

Binary search O(logN):
find the mid, check if mid value is bad,
If mid is bad,
   check the left half
else,
   check the right half
"""
def isBadVersion(V):
   if int(V) >= 50:
      return True
   else:
      return False

def first_bad_version(L):
      return binary_search_helper(L, 0, len(L)-1)

def binary_search_helper(L, left, right):
   while left < right:
      print "left" + str(left)
      print "right" + str(right)
      mid = left + (right - left) // 2
      print "mid" + str(mid)
      if mid == 0:
         print "mid is Zero"
         return L[mid]
      elif isBadVersion(L[mid]) and not isBadVersion(L[mid-1]):
         print "Found first bad version: " + str(L[mid])
         return L[mid]
         break
      elif isBadVersion(L[mid]):
         print "recurse " + str(L[left]) + "to" + str(L[mid])
         return binary_search_helper(L, left, mid)
      else:
         print "recurse " + str(L[mid]) + "to" + str(L[right])
         return binary_search_helper(L, mid, right)
   else:
      return -1
L = [1, 2, 3, 4, 5, 6, 7, 50, 100, 200]
print "First bad version: " + str(first_bad_version(L))
