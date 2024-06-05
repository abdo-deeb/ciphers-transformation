def generate_key_table(key):
    key = ''.join(sorted(set(key), key=key.index))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_table = [[0] * 5 for _ in range(5)]
    key_string = key + ''.join(sorted(set(alphabet) - set(key)))
    for i, char in enumerate(key_string):
        key_table[i // 5][i % 5] = char
    return key_table

def find_position(key_table, char):
    for i, row in enumerate(key_table):
        for j, c in enumerate(row):
            if c == char:
                return i, j

def encrypt_pair(key_table, a, b):
    r1, c1 = find_position(key_table, a)
    r2, c2 = find_position(key_table, b)
    if r1 == r2:
        return key_table[r1][(c1 + 1) % 5] + key_table[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return key_table[(r1 + 1) % 5][c1] + key_table[(r2 + 1) % 5][c2]
    else:
        return key_table[r1][c2] + key_table[r2][c1]

def decrypt_pair(key_table, a, b):
    r1, c1 = find_position(key_table, a)
    r2, c2 = find_position(key_table, b)
    if r1 == r2:
        return key_table[r1][(c1 - 1) % 5] + key_table[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return key_table[(r1 - 1) % 5][c1] + key_table[(r2 - 1) % 5][c2]
    else:
        return key_table[r1][c2] + key_table[r2][c1]

def prepare_text(text, substitute_char='X'):
    text = text.upper().replace('J', 'I')
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = substitute_char
        if a == b:
            prepared += a + substitute_char
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += substitute_char
    return prepared

def encrypt(text, key):
    key_table = generate_key_table(key)
    text = prepare_text(text)
    encrypted = ""
    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(key_table, text[i], text[i + 1])
    return encrypted

def decrypt(text, key):
    key_table = generate_key_table(key)
    decrypted = ""
    for i in range(0, len(text), 2):
        decrypted += decrypt_pair(key_table, text[i], text[i + 1])
    return decrypted
