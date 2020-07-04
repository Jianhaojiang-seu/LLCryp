# from lwe.LWE import Lwe
import sys
from location import Location

class Sender:
    """
    Represents receiver, contains functions to decrypt the cipher

    Attributes
    ----------
    encryption_algorithm : str
        denoted the encryption algorithm used, 'aes' for AES or 'lwe' for LWE

    encrypter : encryption.LWE_Encrypter or encryption.AES_Encrypter object
        denotes the object for the concerned encryption algorithm

    Methods
    -------
    encrypt(location_info=None, raw_data=None)
        Decrypts data according the algorithm used
    """

    encryption_algorithm = "None"
    encrypter = None

    def __init__(self, encryption_algorithm = None, encrypter = None):
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if encrypter is not None:
            self.encrypter = encrypter

    def encrypt(self, location_info, raw_data):
        """
        Encrypts data according the algorithm used

        Parameters
        ---------
            location_info : tuple 
                Location data containing latitude, longitude & tolerance Distance
            raw_data : str
                Data to be encrypted
        
        Returns
        -------
            encrypted_text : binaries
                Encrypted data
            key : binaries
                Key
            iv : binaries
                Initialisation Vector
        """
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(longitude, latitude, tolerance)
        transformed_location = location.getTransformedLocation()
        # TODO: Refactor
        if self.encryption_algorithm is 'aes':
            encrypted_text, key, iv = self.encrypter.encrypt(transformed_location, raw_data)
            return encrypted_text, key, iv
        elif self.encryption_algorithm is 'lwe':
            encrypted_text, key, iv = self.encrypter.encrypt(transformed_location, raw_data)
            return encrypted_text, key, "" 
