import numpy as np
import random
import math

class Receiver:
    """Represents receiver, contains functions to decrypt the cipher
    """

    def decryptMainFile(self, encryptedMainFile, encryptedKey):
        """
            1. get session key by decrypting the encryptedKey
            2. use sessionKey to decrypt the main data file
        """
        sessionKey = self.decryptSessionKey(encryptedKey)
        decryptedMainFile = ""
        return decryptedMainFile


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
        q = self.q
        s = self.s
        for u,v in encryptedKey:
            res=(v-s*u) % q
            binaryData.append(1) if res > q/2 else binaryData.append(0)

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
        A = random.sample(range(q), nvals)

        for x in range(0,len(A)):
        	e.append(random.randint(1,4))
        	B.append((A[x]*s+e[x])%q)

        return (A, B, q)
