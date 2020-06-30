import random
import math
from generateKeys import Keys

class Lwe:
    def LWE_encryption(self, data, secrectKey):
        """ 
        Args:
            data : type - string, data to be encrypted. data = geolockMapping ^ ( sessionKey for encryption of data )

        Returns:
            string: encrypted data
        """
        
        A, B, q = Keys().generatePublicKeys(secrectKey)
        binaryData = self.getBinaryData(data)
        print(binaryData)
        binaryData = str(binaryData)
        encryptedData = [] # list of (u,v) pairs
        for bit in binaryData:
            if bit == ' ':
                encryptedData.append((-1,-1))
                continue
            # sample the numbers from keys
            # print(bit)
            n = len(A)
            sample= random.sample(range(n - 1), n // 4)
            u = 0 
            v = 0
            for x in range(0,len(sample)):
                u = u + A[sample[x]]
                v = v + B[sample[x]]
            v = v + math.floor(q // 2) * (float)(bit)
            v = v % q
            u = u % q
            encryptedData.append((u, v))

        return encryptedData

    def getBinaryData(self, data):
        data = str(data)
        # binaryData = ''.join(format(i, 'b') for i in bytearray(data, encoding ='utf-8')) 
        # binaryData = data.encode('utf-8')
        binaryData = ' '.join(format(ord(i), 'b') for i in data) 
        return binaryData

    def LWE_decryption(self, encryptedData, s, q):
        # s is the secret key
        # q is the modulo number
        binaryData = ''
        for u,v in encryptedData:
            if u==-1 and v==-1:
                binaryData = binaryData + ' '
                continue
                
            res = (v - s * u) % q
            if res > q/2:
                binaryData = binaryData + str(1)
            else:
                binaryData = binaryData + str(0)
        
        print(binaryData)
        decryptedData = self.binaryToString(binaryData)    
        return decryptedData

    def binaryToString(self, binaryData):
        binary_values = binaryData.split()

        ascii_string = ""

        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character

        return ascii_string
