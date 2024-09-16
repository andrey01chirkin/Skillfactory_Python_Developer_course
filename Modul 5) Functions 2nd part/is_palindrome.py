def is_palindrome(word):
    if len(word) == 1: return True
    if word[0] != word[-1]: return False
    return is_palindrome(word[1:-1])


print(is_palindrome('racecar'))
# True
print(is_palindrome('gong'))
# False
