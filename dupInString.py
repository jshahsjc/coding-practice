def dupInString(S):
   NonRep = ""
   Rep = ""
   for i in S:
      if i not in NonRep:
         NonRep = NonRep + i
      elif i not in Rep:
         Rep = Rep + i
   return [Rep, NonRep]

t = 'I am a rockstar..'
print "Repeated: "+dupInString(t)[0]
print "Not repeated: "+dupInString(t)[1]
