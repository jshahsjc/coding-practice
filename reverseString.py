def reverseString(s):
   """
   :type s: List[str]
   :rtype: None Do not return anything, modify s in-place instead.
   """
   k = list(s)
   i = 0
   j = len(k)-1
   while i < j:
      k[i],k[j] = k[j],k[i]
      i+=1
      j-=1
   out = ''.join(k)
   print out
reverseString('Hello')
