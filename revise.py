"""
check if a string is a pallindrome after removing a character
"""

def check_pallindrome(S):
    i = 0
    j = len(S) - 1
    is_pallindrome = True
    while i <= j:
        if S[i] == S[j]:
            i += 1
            j -= 1
        else:
            is_pallindrome = False
            break
    return is_pallindrome

def checkIfPallindrome_after_removing_a_character(S):
    for k in range(len(S) - 1):
        tmpStr = S[:k] + S[k + 1:]
