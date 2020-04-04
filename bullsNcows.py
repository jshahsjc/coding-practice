"""
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates how many digits 
in said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). 
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
"""

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

print "secret: " + "1123"
print "guess: " + "0111"
print "Hint: " + cowsNbulls("1123", "0111")
