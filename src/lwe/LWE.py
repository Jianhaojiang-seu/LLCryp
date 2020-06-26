import random
import math
from lwe.generateKeys import Keys

class Lwe:
    def LWE_encryption(self, data, secrectKey):
        """ 
        Args:
            data : data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

        Returns:
            string: encrypted data
        """
        
        A, B, q = Keys().generatePublicKeys(secrectKey)
        binaryData = self.getBinaryData(data)
        encryptedData = [] # list of (u,v) pairs
        for bit in binaryData:
            # sample the numbers from keys
            n = len(A)
            sample= random.sample(range(n - 1), n // 4)
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

    def LWE_decryption(self, encryptedData, s, q):
        # s is the secret key
        # q is the modulo number
        binaryData = []
        decryptedData = []
        for u,v in encryptedData:
            res = (v - s * u) % q
            binaryData.append(1) if res > q/2 else binaryData.append(0)
        decryptedData = self.binaryToHex(binaryData)            
        return decryptedData

    def binaryToHex(self, binaryData):
        decryptedData = []
        return decryptedData


