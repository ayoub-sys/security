from Cryptodome.Cipher import AES


data=b"heelo world"
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag= cipher.encrypt_and_digest(data)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)