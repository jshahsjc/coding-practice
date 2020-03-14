def checkIfAnagram(S1, S2):
   temp = []
   if len(S1) == len(S2):
      for x in S1:
         if x in S2:
            temp.append(x)
         else:
            break
      if len(temp) == len(S2):
         print "%s and %s are anagrams."%(S1, S2)
      else:
         print "%s and %s are not anagrams."%(S1, S2)

checkIfAnagram("iceman", "cinema")
