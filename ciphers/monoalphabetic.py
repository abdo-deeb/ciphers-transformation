import string

def encrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    substitution = str.maketrans(alphabet, key)
    return text.translate(substitution)

def decrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    reverse_substitution = str.maketrans(key, alphabet)
    return text.translate(reverse_substitution)
