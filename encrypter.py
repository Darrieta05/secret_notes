import rsa

class Encrypter:
    public_key, private_key = rsa.newkeys(512)

    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)
