def romanToInt(s):
   roman_d = {
               'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000
               }
   sum = 0
   i = 0
   while i < len(s):
      if i + 1 < len(s) and roman_d[s[i]] < roman_d[s[i + 1]]:
         sum += roman_d[s[i + 1]] - roman_d[s[i]]
         i += 2
      else:
         sum += roman_d[s[i]]
         i += 1
   return sum

"""
def romanToInt(s):
     values = {
               "I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000,
               }
     total = 0
     i = 0
     while i < len(s):
         # If this is the subtractive case.
         if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
             total += values[s[i + 1]] - values[s[i]]
             i += 2
         # Else this is NOT the subtractive case.
         else:
             total += values[s[i]]
             i += 1
     return total
"""

print romanToInt("MCMXCIV")
