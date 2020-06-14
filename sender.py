class Sender:
    """Represents sender, contains functions to encrypt the message    
    """
    def encrypt(self, location_info, raw_message):
        """Encrypts the raw_message

        Args:
            raw_message (str): Raw un-encrytped message

        Returns:
            string: a list of strings used that are the header columns
        """ 
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        # Apply geoencryption, get location based key
        # get encrypted text
        cipher_text = ""
        return cipher_text
