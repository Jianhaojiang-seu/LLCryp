def LWE_encryption(self, data):
    """ 
    Args:
        data : data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

    Returns:
        string: encrypted data
    """
    A, B, q = fetchPublicKeys()
    binaryData = self.getBinaryData(data)

    encryptedData = [] # list of (u,v) pairs
    for bit in binaryData:
        # sample numbers from keys
        nvals = len(A)
        sample= random.sample(range(nvals - 1), nvals // 4)
        u = 0 
        v = 0
        for x in range(0,len(sample)):
            u = u + A[sample[x]]
            v = v + B[sample[x]]
        v = v + math.floor(q // 2) * bit
        v = v % q
        u = u % q
        encryptedData.append((u, v))
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

def decryptSessionKey(self, encryptedKey):
    """
    Returns:
        string: decrypted message
    """
    geolockMapping = self.getGeoLock()
    decryptedData = self.LWE_decryption(encryptedKey)
    sessionKey = self.getXOR(geolockMapping, decryptedData)
    return sessionKey


def LWE_decryption(self, encryptedKey):
    binaryData = []
    for u,v in encryptedKey:
        res = (v - self.s * u) % self.q
        binaryData.append(1) if res > self.q/2 else binaryData.append(0)
    decyptedData = self.binaryToHex(binaryData)            
    return decyptedData

def binaryToHex(self, binaryData):
    decryptedData = []
    return decryptedData

def getXOR(self, a, b):
    return a^b

def getGeoLock(self):
    """
        Returns: 
            string: geolockMapping
    """
    geolockMapping = ""
    return geolockMapping

def generatePublicKeys(self):
    nvals = 20 # number of values in public key A and B
    B=[]
    e=[]
    self.s = 20
    self.q=97 # modulo number
    A = random.sample(range(self.q), nvals)
    for x in range(0,len(A)):
        e.append(random.randint(1,4))
        B.append((A[x]* self.s + e[x]) % self.q)
    return (A, B, self.q)
