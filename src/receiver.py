from location import Location
# from src.lwe.LWE import Lwe

class Receiver:
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
    decrypt(location_info=None, decryption_data=None)
        Decrypts data considering the location of the receiver & tolerance distance
    """

    encryption_algorithm = None
    encrypter = None

    def __init__(self, encryption_algorithm = None, encrypter = None):
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if encrypter is not None:
            self.encrypter = encrypter

    def decrypt(self, location_info, decryption_data):
        """
        Decrypts data according the algorithm used

        Parameters
        ---------
            location_info : tuple 
                Location data containing latitude, longitude & tolerance Distance
            decryption_data : tuple
                Contains Encrypted text & original key-hash as received from sender
        
        Returns
        -------
            tuple
                (bool -- True if data is decrypted, str -- Decrypted data)        
        """
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(longitude, latitude, tolerance)
        transformed_location = location.getTransformedLocation()

        # TODO: Refactor
        if self.encryption_algorithm is 'aes':
            encryted_data = decryption_data[0]
            key = decryption_data[1]
            iv = decryption_data[2]
            transformed_loc_adj = location.getAdjacentQuadrants()
            decrypted_text = None
            # BUG: tolerance distance factor is not working correctly.
            for transformed_location in transformed_loc_adj:    
                # Checking all the 8 octants
                decrypted_text = self.encrypter.decrypt(transformed_location, encryted_data, key, iv)
                # Debug Point: print (decrypted_text)
                if decrypted_text is not None:
                    break
            return ((decrypted_text != None), decrypted_text)
        
        elif self.encryption_algorithm is 'lwe':
            encryted_data = decryption_data[0]
            secret_key = decryption_data[1]
            q = decryption_data[2]
            transformed_loc_adj = location.getAdjacentQuadrants()
            decrypted_text = None
            for transformed_location in transformed_loc_adj:
                # Checking all the 8 octants
                decrypted_text = self.encrypter.decrypt(transformed_location, encryted_data, q, secret_key)
                # Debug Point: print (decrypted_text)
                if decrypted_text is not None:
                    break
            return ((decrypted_text != None), decrypted_text)
