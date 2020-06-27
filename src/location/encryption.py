from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode


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
        # print(key)
        # print("\n\n")
        cipher = AES.new(key, AES.MODE_CBC) # TODO (Less Priority for now): Use IV (Initialisation Vector)
        encrypted_text_bytes = cipher.encrypt(pad(data, AES.block_size)) # Or Cipher Text
        iv = b64encode(cipher.iv).decode('utf-8')
        encrypted_text = b64encode(encrypted_text_bytes).decode('utf-8')
        return encrypted_text, key, iv


    def decrypt(self, transformed_location = None, encrypted_text = None, original_key = None, iv=None):
        decrypted_text_bytes = None
        if original_key == self.deriveKey(transformed_location):
            iv = b64decode(iv)
            encrypted_text = b64decode(encrypted_text)
            cipher = AES.new(original_key, AES.MODE_CBC, iv)
            decrypted_text_bytes = unpad(cipher.decrypt(encrypted_text), AES.block_size)
        else:
            pass
        return decrypted_text_bytes
