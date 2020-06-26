# from lwe.LWE import Lwe

import sys
from location import Location
from encryption import Encrypter

class Sender:
    """Represents sender, contains functions to encrypt the message    
    """
    encrypter = None

    def __init__(self, encrypter = None):
        if encrypter is not None:
            self.encrypter = encrypter

    def encrypt(self, location_info, raw_message):
        """Encrypts the raw_message

        Args:
            location_info (tuple): Location data containing latitude, longitude & tolerance Distance
            raw_message (str): Raw non-encrypted data 

        Returns:
            string: a list of strings used that are the header columns
        """
        #  location = Location(latitude, longitude, tolerance)
        #  secretKey = location.getTransformedLocation()
        #  encryptionTool = Lwe()
        #  cipher_text = encryptionTool.LWE_encryption(raw_message, secretKey)
        #  return cipher_text
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(longitude, latitude, tolerance)
        transformed_location = location.getTransformedLocation()
        encrypted_text = self.encrypter.encrypt(transformed_location, raw_message)
        return encrypted_text
