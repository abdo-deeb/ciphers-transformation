from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text.encode(), DES.block_size))
    return encrypted_text.hex()

def decrypt(text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(bytes.fromhex(text)), DES.block_size)
    return decrypted_text.decode()
