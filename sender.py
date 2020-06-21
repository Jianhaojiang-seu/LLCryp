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

        geolockMapping = self.createGeoLock(longitude, latitude, tolerance)
        sessionKey = self.getSessionKey()
        data = self.getXOR(geolockMapping, sessionKey)

        # get encrypted text
        cipher_text = self.LWE(data)
        return cipher_text

    def LWE(self, data):
        """ 
        Args:
            data : data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

        Returns:
            string: encrypted data
        """
        encryptedData = ""

        return encryptedData

    def createGeoLock(self, longitude, latitude, tolerance):
        """
            Returns: 
                string: geolockMapping
        """
        geolockMapping = ""
        return geolockMapping

    def getXOR(self, geolockMapping, sessionKey):
        return geolockMapping ^ sessionKey

    def getSessionKey(self):
        """
            This key would be used for encryption of main data i.e this key will be used for symmetric encryption. We would secure this 
            key using LWE.
        """
        sessionKey = " "
        return sessionKey


        
