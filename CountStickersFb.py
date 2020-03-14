# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word
#'facebook', outputs an integer with the number of # stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook'
#letters, and the only potential non-letter characters
# in the string are spaces.

def count_chars_in_string(S):
   res = {}
   for k in S:
      if k != ' ':
         if k not in res:
            res[k] = 1
         else:
            res[k] += 1
   return res

def get_num_stickers(baseCharCount, givenCharCount):
   count = 0
   for k in givenCharCount:
      p = givenCharCount[k]/baseCharCount[k]
      if p > count:
         count = p
   return count


sticker1 = 'facebook'
stickers = ['coffee kebab', 'book', 'ffacebook']

sticker1Chars = count_chars_in_string(sticker1)

for sticker in stickers:
   stickerChars = count_chars_in_string(sticker)
   print sticker + ":" + str(get_num_stickers(sticker1Chars, stickerChars))
