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
   while len(L) >= 1:
      print "========="
      mid = len(L) // 2
      LeftList = L[:mid]
      RightList = L[mid:]
      print L
      print "mid is " + str(mid)
      print "LeftList is " + str(LeftList)
      print "RightList is " + str(RightList)

      # if mid is zero, we have found the first bad value, return it.
      if mid is 0:
         print "mid is zero, return value at mid."
         return L[mid]
      # First handle the case when you have a clear split
      # so, this is the optimum case where you check the value at mid is
      # bad and if value at (mid - 1) is good, so you know right away that
      # value at mid is the first bad value. No need of further
      # processing. This check helps minimize API calls.
      elif isBadVersion(L[mid]) and not isBadVersion(L[mid - 1]):
         print str(L[mid]) + str(isBadVersion(L[mid])) + str(L[mid-1]) + str(isBadVersion(L[mid - 1]))
         return L[mid]
         break
         print str(L[mid])+ " is " + str(isBadVersion(L[mid]))

      # Now we check if the mid is not zero
      else:
         # if value at mid is bad, recurse on left list
         if isBadVersion(L[mid]):
            print "mid not zero, mid is bad, recurse on LeftList"
            return first_bad_version(LeftList)
         # if the value at mid is good, recurse on the right list
         else:
            print "mid not zero, mid is good, recurse on RightList"
            return first_bad_version(RightList)
            print "========="

L = [1, 2, 3, 4, 5, 6, 7, 50, 100, 200]
print "First bad version: " + str(first_bad_version(L))
