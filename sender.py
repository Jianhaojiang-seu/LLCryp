from fetchKeys import fetchPublicKeys
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

    def LWE_encryption(self, data):
        """ 
        Args:
            data : data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

        Returns:
            string: encrypted data
        """
        A, B, moduloNumber = fetchPublicKeys()
        binaryData = self.getBinaryData()

        encryptedData = [] # list of (u,v) pairs
        for bit in binaryData:
            # sample numbers from keys
            nvals = len(A)
            sample= random.sample(range(nvals-1), nvals//4)
            u = 0 
            v = 0
            for x in range(0,len(sample)):
            	u = u + A[sample[x]
            	v = v + B[sample[x]]
            v = v + math.floor(q//2)*message
            v = v % q
            u = u % q
            encryptedData.append((u,v))
        return encryptedData

    def getBinaryData(self, data):
        binaryData = ""
        return binaryData

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


        
