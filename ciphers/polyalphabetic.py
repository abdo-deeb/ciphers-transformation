def polyalphabetic_encrypt(plain_text, shifts_input):
    encrypted_text = ""
    shifts = list(map(int, shifts_input.split()))
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = shifts[i % len(shifts)]
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((ord(char) - base + shift) % 26) + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text
def polyalphabetic_decrypt(encrypted_text, shifts):
    decrypted_text = ""
    shifts = list(map(int, shifts.split()))
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift = shifts[i % len(shifts)]
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text