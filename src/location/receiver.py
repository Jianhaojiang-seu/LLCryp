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
        location = Location(longitude, latitude, tolerance)
        transformed_location = location.getTransformedLocation()
        encryted_data = decryption_data[0]
        key = decryption_data[1]
        iv = decryption_data[2]
        transformed_loc_adj = location.getAdjacentQuadrants()
        decrypted_text = None
        # BUG: tolerance distance factor is not working correctly.
        for transformed_location in transformed_loc_adj:
            decrypted_text = self.encrypter.decrypt(transformed_location, encryted_data, key, iv)
            if decrypted_text is not None:
                break
        if decrypted_text is None:
            print('The data can\'t be decrypted')
        else:
            print('The decrypted text is: ', decrypted_text, sep=" ")