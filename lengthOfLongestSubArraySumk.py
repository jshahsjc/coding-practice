"""
def lengthOfLogestSubArrSumK(nums, k):
   prev_sums = {}
   curr_sum = 0
   max_len = 0
   for i, n in enumerate(nums):
      curr_sum += n

      if curr_sum == k:
         max_len = i + 1

      if  (curr_sum - k) in prev_sums:
         max_len = max(max_len, i - prev_sums[curr_sum - k])
      else:
         prev_sums[curr_sum] = i

   return max_len
"""
def lenOfLongestSubstrSumK(nums, k):
   max_len = 0
   prev_sum = {}
   curr_sum = 0

   for i, val in enumerate(nums):
      curr_sum += val

      if curr_sum == k:
         max_len = i + 1

      if (curr_sum - k) in prev_sum:
         max_len = max(max_len, i - prev_sum[curr_sum - k])
      else:
         prev_sum[curr_sum] = i

   return max_len

arr = [10, 5, 2, 7, 1, 9]
k = 15

print lenOfLongestSubstrSumK(arr, k)
