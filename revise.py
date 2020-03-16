"""
function 1: compare two given strings, return true if sorted

function 2: for k in range(len(list)-1),
            check if function1 (list[k], list[k+1]) returns false, break,
            else return True (sorted)

Also for each of the contraints, assert if condition isn't satisfied

function 1:
   find shorter length: compare and record shorter length out of the two given strings. This will be our traversal length.
   for var in traversal length,
      condition1:
      compare the letter at given var position,
         if not same,  if first is lower than seccond, return True
                       else False
      condition 2:
         if all letters are same, if first string is shorter than second, return True (sorted). else, False (unsorted).

"""

def alien_dict_check(words, order):

   for i in range(len(words)-1):
      result = compare_words(words[i], words[i+1], order)
      if result == False:
         return False
         break
      else:
         return True

def compare_words(word1, word2, order):
   is_sorted = False
   comp_order = get_order_dict(order)
   comp_len = get_traversal_len(word1, word2)

   if word1[:comp_len] == word2[:comp_len] and len(word1) <= len(word2):
      is_sorted = True
   else:
      for k in range(comp_len):
         if comp_order[word1[k]] < comp_order[word2[k]]:
            is_sorted = True
            break

   return is_sorted

def get_traversal_len(word1, word2):
   if len(word1) <= len(word2):
      return len(word1)
   else:
      return len(word2)

def get_order_dict(order):
   order_dict = {}
   v = 0
   for k in order:
      order_dict[k] = v
      v += 1
   return order_dict


print "Input: " + 'words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"'
print "Sorted ? " + str(alien_dict_check(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))

print "Input: " + 'words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"'
print "Sorted ? " + str(alien_dict_check(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))

print "Input: " + 'words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"'
print "Sorted ? " + str(alien_dict_check(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
