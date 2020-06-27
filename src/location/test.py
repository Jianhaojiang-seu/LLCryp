from sender import Sender
from receiver import Receiver
from location import Location
from encryption import Encrypter

if __name__ == "__main__":
    message = "Only if we remember to turn on the light"
    location_info = [12, 13, 1]
    encrypter = Encrypter()
    sender1 = Sender(encrypter)
    encrypted_text1, key1, iv1 = sender1.encrypt([16, 16, 1], message)
    receiver1 = Receiver(encrypter)
    receiver1.decrypt([16, 16, 1], [encrypted_text1, key1, iv1])    # BUG: Tolerance Distance factor is not working as expected
