def is_anagram(words):
    if sorted(words[0]) == sorted(words[1]):
        return True
    else:
        return False

