def cowsNbulls(secret, guess):
   """
   type secret: str
   type guess: str
   """

   secret_list = list(str(secret))
   guess_list = list(str(guess))
   seen_secrets = []
   seen_guesses = []
   bull_count = 0
   cow_count = 0

   for i in range(len(guess_list)):
      if guess_list[i] == secret_list[i]:
         bull_count += 1
      else:
         seen_secrets.append(secret_list[i])
         seen_guesses.append(guess_list[i])

   for guess in seen_guesses:
      if guess in seen_secrets:
         cow_count += 1
         seen_secrets.remove(guess)

   return str(bull_count) + "A" + str(cow_count) + "B"

print "secret: " + "1807"
print "guess: " + "7810"
print "Hint: " + cowsNbulls("1807", "7810")
