from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text.encode(), AES.block_size))
    return encrypted_text.hex()

def decrypt(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(bytes.fromhex(text)), AES.block_size)
    return decrypted_text.decode()
