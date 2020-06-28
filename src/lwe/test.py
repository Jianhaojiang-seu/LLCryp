# from fetchKeys import fetchPublicKeys
# import math
# import random

# print(transformed_location)
# geolockMapping = self.createGeoLock(longitude, latitude, tolerance)
# sessionKey = self.getSessionKey()
# data = self.getXOR(geolockMapping, sessionKey)
# cipher_text = self.LWE_encryption(data)


from LWE import Lwe

L = Lwe()
data = '122'
secrectKey = 20000.0234352
encryptedData = L.LWE_encryption(data, secrectKey)
print(encryptedData)

decryptedData = L.LWE_decryption(encryptedData, secrectKey, 97)
print(decryptedData)

# data = 'my name is yash`'

# s = data.encode('utf-8')
# print(s)
# print( s.decode('utf-8') )
