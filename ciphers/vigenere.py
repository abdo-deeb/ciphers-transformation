def extend_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    key = extend_key(text, key)
    cipher_text = ""
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text += chr(x)
    return cipher_text

def decrypt(text, key):
    key = extend_key(text, key)
    orig_text = ""
    for i in range(len(text)):
        x = (ord(text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text += chr(x)
    return orig_text
