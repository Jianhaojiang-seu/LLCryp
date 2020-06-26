from location import Location
# from src.lwe.LWE import Lwe

class Receiver:
    """Represents receiver, contains functions to decrypt the cipher
    """

    encrypter = None

    def __init__(self, encrypter = None):
        if encrypter is not None:
            self.encrypter = encrypter

    def decrypt(self, location_info, decryption_data):
        """
        Args:
            location_info (tuple): Location data containing latitude, longitude & tolerance Distance
            decryption_data (tuple): Contains Encrypted text & original key-hash as received from sender
        """

        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(latitude, longitude, tolerance)
        encryted_data = decryption_data[0]
        key = decryption_data[1]
        # Call the decrypter here & verify results



