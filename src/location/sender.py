from location import Location
from src.lwe.LWE import Lwe
class Sender:
    """Represents sender, contains functions to encrypt the message    
    """

    def encryptData(self, location_info, raw_message):
        """Encrypts the raw_message

        Args:
            raw_message (str): Raw un-encrytped message 

        Returns:
            string: a list of strings used that are the header columns
        """ 
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(latitude, longitude, tolerance)
        secretKey = location.getTransformedLocation()
        encryptionTool = Lwe()
        cipher_text = encryptionTool.LWE_encryption(raw_message, secretKey)
        return cipher_text
