import re

# 5
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram("Listen", "Silent"))  
print(is_anagram("Hello", "World"))    

# 6
def is_strong_password(password):
    if (len(password) < 8):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

print(is_strong_password("Ps!0sldksa")) 
print(is_strong_password("veryweak"))   

# 7
def find_longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


sentence = "Find the longest word in this sentence"
print(find_longest_word(sentence))  

# 8
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, 3], [4, [5, 6]]]
print(flatten_list(nested)) 