from location import Location
from src.lwe.LWE import Lwe

class Receiver:
    """Represents receiver, contains functions to decrypt the cipher
    """

    def decryptData(self, encryptedData, moduloNumber):
        """
            1. get session key by decrypting the encryptedKey
            2. use sessionKey to decrypt the main data file
        """
        latitude, longitude, tolerance =  self.getMyLocation()
        location = Location(latitude, longitude, tolerance)
        keyInputs = location.getAdjacentQuadrants()
        decryptionTool = Lwe()
        for key in keyInputs:
            result = decryptionTool.LWE_decryption(encryptedData, key, moduloNumber)
            if result:
                return result
            else:
                return "you are not in the correct location"

    def getMyLocation(self):
        latitude = ""
        longitude = ""
        tolerance = ""
        return (latitude, longitude, tolerance)


