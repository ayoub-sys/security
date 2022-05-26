from cryptography.fernet import Fernet
key=Fernet.generate_key()
fernet =Fernet(key)
message=b"hello ayoub"
encrypted_message1=fernet.encrypt(message)
encrypted_message2=fernet.encrypt(message)
print(message)
print("\n")
print(encrypted_message1)
print(encrypted_message2)
decrypted_message1=fernet.decrypt(encrypted_message1)
decrypted_message2=fernet.decrypt(encrypted_message2)
print(decrypted_message1)
print(decrypted_message2)