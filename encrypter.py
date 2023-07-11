import rsa

class Encrypter():
    public_key, private_key = rsa.newkeys(512)

    def __init__(self):
        encrypter_type = "bytes"

    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)

    def decrypt(self, bytes):
        return rsa.decrypt(bytes, self.private_key).decode()
    
