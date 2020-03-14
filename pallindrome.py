def reverseString(S):
   L = list(str(S))
   print L
   i, j = 0, len(L)-1
   if len(L) > 1:
      while i < j:
         L[i], L[j] = L[j], L[i]
         i += 1
         j -= 1
      return str("".join(L))
   elif len(L) == 1:
      return L
   else:
      return None

def checkPallindrom(S):
   if reverseString(S) == S:
      print "%s is a pallindrome."%S
   else:
      print "%s is not a pallindrome."%S

t = "wow"
checkPallindrom(t)
