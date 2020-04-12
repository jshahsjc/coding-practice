"""
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation:
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
Example 2:

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]
Example 3:

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]
"""

"""
Approach:
Use binary search on stores, to get a floor and ceiling of each house,
return minimum of floor or ceiling
"""

class Solution(object):
   def storesAndHouses(self, houses, stores):
      """
      type: houses: list
      type: stores: list
      rtype: list
      """
      def getFloor(arr, low, high, x):
         # if x is greater than high, high is floor
         if x >= arr[high]:
            return high
         if x == arr[low]:
            return low
         # if low is greater than high, return -1
         if low > high or x < arr[low]:
            return None
         # get the mid value
         mid = low + (high - low) // 2
         # check if mid is x,  mid is floor
         if arr[mid] <= x < arr[mid + 1]:
            return mid
         # check if x is between mid - 1 and mid
         if mid > 0 and  arr[mid - 1] < x < arr[mid]:
            return mid - 1
         # if x is less than mid, check on left half
         if x < arr[mid]:
            return getFloor(arr, low, mid - 1, x)
         if arr[mid] < x < arr[high]:
            return getFloor(arr, mid + 1, high, x)

      def getCeiling(arr, low, high, x):
         # if x is lower than low, ceiling is low
         if x <= arr[low]:
            return low
         # if x is high, ceiling is high
         if x == arr[high]:
            return high
         # if x is greater than high, return -1
         if x > arr[high] or low > high:
            return None
         # get the mid value
         mid = low + (high - low) // 2
         # check if mid value is x
         if arr[mid - 1] < x <= arr[mid]:
            return mid
         # check if x is between mid and mid + 1
         if mid > 0 and arr[mid] < x <= arr[mid + 1]:
            return mid + 1
         # if x is greater than mid + 1 value, recurse right
         if arr[mid] < x < arr[high]:
            return getCeiling(arr, mid + 1, high, x)
         # if x is less than mid, recurse left
         if arr[low] < x < arr[mid]:
            return getCeiling(arr, low, mid - 1, x)

      res = []
      stores.sort()
      print "houses: " +str(houses)
      print "stores sorted: " + str(stores)
      for house in houses:
         ceiling = getCeiling(stores, 0, len(stores) - 1, house)
         floor = getFloor(stores, 0, len(stores) - 1, house)
         if ceiling is not None and floor is not None:
            print str(house)+ " ceiling:" + str(stores[ceiling])
            print str(house) + " floor:" + str(stores[floor])
            diff_ceiling = stores[ceiling] - house
            diff_floor = house - stores[floor]
            if diff_ceiling < diff_floor:
               res.append(stores[ceiling])
            elif diff_floor < diff_ceiling:
               res.append(stores[floor])
            elif diff_floor == diff_ceiling:
               if ceiling != floor:
                  eq_diff_stores = min(stores[floor], stores[ceiling])
                  print "Min of equidistant stores: " + str(eq_diff_stores)
                  res.append(eq_diff_stores)
               else:
                  res.append(stores[floor])
         elif ceiling is not None:
            print str(house)+ " ceiling:" + str(stores[ceiling])
            res.append(stores[ceiling])
         elif floor is not None:
            print str(house)+ " floor:" + str(stores[floor])
            res.append(stores[floor])
         else:
            pass

      return res

houses = [4, 8, 1, 1]
stores = [5, 3, 1, 2, 6]

houses1 = [2, 4, 2]
stores1 = [5, 1, 2, 3]

houses2 = [5, 10, 17]
stores2 = [1, 5, 20, 11, 16]

s = Solution()
print "++++++++++++++++++++++++++++++++++"
print s.storesAndHouses(houses, stores)
print "++++++++++++++++++++++++++++++++++"
print s.storesAndHouses(houses1, stores1)
print "++++++++++++++++++++++++++++++++++"
print s.storesAndHouses(houses2, stores2)
print "++++++++++++++++++++++++++++++++++"
