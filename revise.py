def findTwoSum(given_nums, target):
   res = {}

   for i, num in enumerate(given_nums):
      comp = target - num
      if comp not in res:
         res[num] = i
      else:
         return [res[comp], i]
