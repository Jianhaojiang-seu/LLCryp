import random
import math

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode

class AES_Encrypter:
    """
    AES Encrypter & its helper functions

    Attributes
    ----------
    salt : bytes
        salt used for encryption

    Methods
    -------
    deriveKey(transformed_location=None)
        Derives key from location using PBKDF2

    encrypt(transformed_location=None, raw_text=None)
    """
    salt = None

    def __init__(self):
        self.salt = get_random_bytes(16)

    def deriveKey(self, transformed_location=None):
        """ Derive a key of size 16 bytes using PBKDF2 Algorithm
        """
        def convertLocationToString(transformed_location):
            """ To convert the transformed_location to a string, which is used to derive 16 byte key
            """
            result_string = str(transformed_location[0]) + " " + str(transformed_location[1])
            return result_string
        transformed_loc_string = convertLocationToString(transformed_location)
        transformed_loc_string = str.encode(transformed_loc_string)
        key = PBKDF2(transformed_loc_string, self.salt, 16, count=100)
        return key

    def encrypt(self, transformed_location=None, raw_text=None):
        """Ref: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html
        """
        data = str.encode(raw_text)
        key = self.deriveKey(transformed_location)
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

class LWE_Encrypter:
    """
    LWE Encrypter & its helper functions

    Attributes
    ----------
    salt : bytes
        salt used for encryption

    Methods
    -------
    generateSecretKey(transformed_location=None)
        Derives key from location using PBKDF2

    generatePublicKeys(secret_key=None)
        Derives Public Keys to be used in LWE from Secret Key

    encrypt(transformed_location=None, data=None)
        Encrypts the data
    
    decrypt(self, transformed_location = None, encrypted_data = None, q = None, original_key = None)
        Decrypts the data
    """

    salt = None

    def __init__(self):
        self.salt = get_random_bytes(16)

    def generateSecretKey(self, transformed_location=None):
        def convertLocationToString(transformed_location):
            """ To convert the transformed_location to a string, which is used to derive 16 byte key
            """
            result_string = str(transformed_location[0]) + " " + str(transformed_location[1])
            return result_string
        transformed_loc_string = convertLocationToString(transformed_location)
        transformed_loc_string = str.encode(transformed_loc_string)
        key = PBKDF2(transformed_loc_string, self.salt, 4, count=100)
        return int.from_bytes(key, byteorder='big') # Hacky fix for generating int key

    def generatePublicKeys(self, secret_key):
        n = 20 # number of values in public key A and B
        B = []
        e = []
        s = secret_key
        q = 97 # modulo number
        A = random.sample(range(q), n)
        for x in range(0,len(A)):
            e.append(random.randint(1,4))
            B.append((A[x]*s + e[x]) % q)
        return (A, B, q)

    def encrypt(self, transformed_location=None, data=None):
        """ 
        Args:
            data : type - string, data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

        Returns:
            string: encrypted data
        """
        secret_key = self.generateSecretKey(transformed_location)
        A, B, q = self.generatePublicKeys(secret_key)
        binary_data = self.getBinaryData(data)
        # Debug Point print(binary_data)
        binary_data = str(binary_data)
        encrypted_data = [] # list of (u,v) pairs
        for bit in binary_data:
            if bit == ' ':
                encrypted_data.append((-1,-1))
                continue
            n = len(A)
            sample = random.sample(range(n - 1), n // 4)   # Sampling the number of keys
            u = 0 
            v = 0
            for x in range(0,len(sample)):
                u = u + A[sample[x]]
                v = v + B[sample[x]]
            v = v + math.floor(q // 2) * (float)(bit)
            v = v % q
            u = u % q
            encrypted_data.append((u, v))
        return encrypted_data, secret_key, ""

    def getBinaryData(self, data):
        data = str(data)
        binary_data = ' '.join(format(ord(i), 'b') for i in data) 
        return binary_data

    def decrypt(self, transformed_location = None, encrypted_data = None, q = None, original_key = None):
        """
        Args:
            q - {int} - Modulo Number
        """
        if self.generateSecretKey(transformed_location) == original_key:     
            s = self.generateSecretKey(transformed_location)    # Secret Key
            binary_data = ''
            for u,v in encrypted_data:
                if u==-1 and v==-1:
                    binary_data = binary_data + ' '
                    continue
                res = (v - s * u) % q
                if res > q/2:
                    binary_data = binary_data + str(1)
                else:
                    binary_data = binary_data + str(0)
            decryptedData = self.binaryToString(binary_data)    
            return decryptedData
        else:
            return None

    def binaryToString(self, binary_data):
        binary_values = binary_data.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
        return ascii_string
