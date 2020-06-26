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


