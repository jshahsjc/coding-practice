"""
You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"
"""

def maximumTime(T):
   hour = T.split(":")[0]
   min = T.split(":")[1]
   max_hour = ["2","3"]
   max_min = ["5","9"]

   if hour[0] != '?' and hour[1] != '?':
      max_hour = hour.split()
   elif hour[0] == '?' and hour[1] != '?':
      max_hour[1] = hour[1]
      if int(hour[1]) <= 3:
         max_hour[0] = '2'
      else:
         max_hour[0] = '1'
   elif hour[0] != '?' and hour[1] == '?':
      max_hour[0] = hour[0]
      if int(hour[0]) <= 1:
         max_hour[1] = '9'
      else:
         max_hour[1] = '3'
   else:
      pass

   if min[0] != '?' and min[1] != '?':
      max_min = min.split()
   elif min[0] == '?' and min[1] != '?':
      max_min[0] == '5'
   elif min[0] != '?' and min[1] == '?':
      max_min[1] == '9'
   else:
      pass

   return ("".join(max_hour) + ":" + "".join(max_min))

input = ["0?:??", "??:??", "2?:22", "23:5?", "?4:5?"]
for t in input:
   print  "input: " + t + " -->  output: " + maximumTime(t)
