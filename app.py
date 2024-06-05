from flask import Flask, render_template, request, jsonify
from ciphers import (
    caesar_encrypt, caesar_decrypt,
    monoalphabetic_encrypt, monoalphabetic_decrypt,
    playfair_encrypt, playfair_decrypt,
    polyalphabetic_encrypt, polyalphabetic_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    rail_fence_encrypt, rail_fence_decrypt,
    row_transposition_encrypt, row_transposition_decrypt,
    des_encrypt, des_decrypt,
    aes_encrypt, aes_decrypt
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    action = request.form['action']
    cipher = request.form['cipher']
    text = request.form['text']
    key = request.form.get('key', '')

    try:
        if action == 'encrypt':
            if cipher == 'caesar':
                result = caesar_encrypt(text, int(key))
            elif cipher == 'monoalphabetic':
                result = monoalphabetic_encrypt(text, key)
            elif cipher == 'playfair':
                result = playfair_encrypt(text, key)
            elif cipher == 'polyalphabetic':
                result = polyalphabetic_encrypt(text, key)
            elif cipher == 'vigenere':
                result = vigenere_encrypt(text, key)
            elif cipher == 'rail_fence':
                result = rail_fence_encrypt(text, int(key))
            elif cipher == 'row_transposition':
                result = row_transposition_encrypt(text, key)
            elif cipher == 'des':
                result = des_encrypt(text, key)
            elif cipher == 'aes':
                result = aes_encrypt(text, key)
        elif action == 'decrypt':
            if cipher == 'caesar':
                result = caesar_decrypt(text, int(key))
            elif cipher == 'monoalphabetic':
                result = monoalphabetic_decrypt(text, key)
            elif cipher == 'playfair':
                result = playfair_decrypt(text, key)
            elif cipher == 'polyalphabetic':
                result = polyalphabetic_decrypt(text, key)
            elif cipher == 'vigenere':
                result = vigenere_decrypt(text, key)
            elif cipher == 'rail_fence':
                result = rail_fence_decrypt(text, int(key))
            elif cipher == 'row_transposition':
                result = row_transposition_decrypt(text, key)
            elif cipher == 'des':
                result = des_decrypt(text, key)
            elif cipher == 'aes':
                result = aes_decrypt(text, key)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
