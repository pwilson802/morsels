def is_anagram(*words):
    w = [''.join(x for x in i if x.isalpha()) for i in words]
    if sorted(w[0].lower()) == sorted(w[1].lower()):
        return True
    else:
        return False

from collections import Counter
def is_anagram2(*words):
    if Counter(words[0].lower()) == Counter(words[1].lower()):
        return True
    else:
        return False