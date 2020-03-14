"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 26,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
Approach:
Brute Force:
   For each element in the array,
      try adding with rest of the elements from the elements except itself
      if the sum = given value than break
   return indices

Problem is that some of the pair will repeat, for example 2 + 7 is not 26,
However, we'll also do 7 + 2 for 7, which is not required.

Try another method:
start with index 0, iterate 1 to 3 (0+1, 0+2, 0+3)
increment index 1, iterate 2 to 3 (1+2, 1+3)
increment index 2, iterate 3 (2+3)
for each pair, compare with target, if hit, break.

So, given 4 numbers, there are 6 possible pairs -- O[n(n-1)/2]

"""

def findTwoSum(given_nums, target):
   for i in range(len(given_nums)):
      for j in range (i+1, len(given_nums)):
         k = given_nums[i] + given_nums[j]
         if k == target:
            return (i, j)
            break
   else:
      return ("No match found")


my_num = [2, 7, 11, 15, 100, 350, 0, -40, -4]
t = 101

result_pair = findTwoSum(my_num, t)
print "given nums: " + str(my_num)
print "target: " + str(t)
print "result pair: " + str(result_pair)
