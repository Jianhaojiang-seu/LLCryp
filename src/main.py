from sender import Sender
from receiver import Receiver
from location import Location
from encryption import AES_Encrypter, LWE_Encrypter

if __name__ == "__main__":
    message1 = "Happiness can be found in darkest of times"
    message2 = "Only if we remember to turn on the light"
    # location_info = [12, 13, 1]

    # AES Encryption
    print("Running AES")
    aes_encrypter = AES_Encrypter()
    sender1 = Sender('aes', aes_encrypter)
    encrypted_text1, key1, iv1 = sender1.encrypt([12, 45, 1], message1)
    print("Encrypted Text (AES):", encrypted_text1, sep=" ", end="\n")
    receiver1 = Receiver('aes', aes_encrypter)
    decrypted_data1 = receiver1.decrypt([12, 45, 1], [encrypted_text1, key1, iv1])    # BUG: Tolerance Distance factor is not working as expected
    if decrypted_data1[0]:
        print("Decrypted Text (AES):", decrypted_data1[1].decode('ascii'), sep=" ", end="\n\n")
    else:
        print("The Text cannot be decrypted")

    print('\n\n')
    for _ in range(150):
        print('-', end="")
    print('\n\n')

    # LWE Encryption
    print("Running LWE")
    lwe_encrypter = LWE_Encrypter()
    sender2 = Sender('lwe', lwe_encrypter)
    encrypted_text2, key2, iv2 = sender2.encrypt([11, 65, 1], message2)
    print("Encrypted Text (AES):", encrypted_text2, sep=" ", end="\n")
    receiver2 = Receiver('lwe', lwe_encrypter)
    decrypted_data2 = receiver2.decrypt([11, 65, 1], [encrypted_text2, key2, 97])
    if decrypted_data2[0]:
        print("Decrypted Text (LWE):", decrypted_data2[1], sep=" ", end="\n\n")
    else:
        print("The Text cannot be decrypted")
