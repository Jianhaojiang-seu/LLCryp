class Receiver:
    """Represents receiver, contains functions to decrypt the cipher
    """
    def decrypt(self, location_info, encrypted_text):
        """Encrypts the raw_message

        Args:
            location_info (tuple) : Geoencyption parameters
            raw_message (str): Raw un-encrytped message

        Returns:
            string: a list of strings used that are the header columns
        """ 
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        # Apply geoencryption, get location based key
        # get encrypted text
        decrypted_text = ""
        return decrypted_text
