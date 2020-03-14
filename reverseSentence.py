def reverseSentence(S):
   L = S.split(" ")
   if len(L) > 1:
      i, j = 0, len(L)-1
      while i < j:
         L[i], L[j] = L[j], L[i]
         i += 1
         j -= 1
   return " ".join(L)

t = "it was a sunny day"
print reverseSentence(t)
