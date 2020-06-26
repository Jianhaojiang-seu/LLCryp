from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

class Encrypter:
    salt = None

    def __init__(self):
        self.salt = get_random_bytes(16)

    def convertLocationToString(self, transformed_location):
        """ To convert the transformed_location to a string, which is used to derive 16 byte key
        """
        result_string = str(transformed_location[0]) + " " + str(transformed_location[1])
        return result_string


    def deriveKey(self, transformed_location):
        """ Derive a key of size 16 bytes using PBKDF2 Algorithm
        """
        transformed_loc_string = self.convertLocationToString(transformed_location)
        transformed_loc_string = str.encode(transformed_loc_string)
        key = PBKDF2(transformed_loc_string, self.salt, 16, count=100)
        return key

    def encrypt(self, transformed_location, raw_text):
        """Ref: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html
        """
        data = str.encode(raw_text)
        key = self.deriveKey(transformed_location)
        cipher = AES.new(key, AES.MODE_CBC) # TODO (Less Priority for now): Use IV (Initialisation Vector)
        encrypted_text = cipher.encrypt(pad(data, AES.block_size)) # Or Cipher Text
        return encrypted_text, key


    def decrypt(self, ):
        pass