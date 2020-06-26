from fetchKeys import fetchPublicKeys
import math
import random

class Sender:
    """Represents sender, contains functions to encrypt the message    
    """

    def encryptMainFile(self, data):
        encryptedMainFile = ""
        return encryptedMainFile

    def encryptSessionKey(self, location_info, raw_message):
        """Encrypts the raw_message

        Args:
            raw_message (str): Raw un-encrytped message 

        Returns:
            string: a list of strings used that are the header columns
        """ 
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]

        geolockMapping = self.createGeoLock(longitude, latitude, tolerance)
        sessionKey = self.getSessionKey()
        data = self.getXOR(geolockMapping, sessionKey)

        # get encrypted text
        cipher_text = self.LWE_encryption(data)
        return cipher_text
