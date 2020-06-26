from sender import Sender
from receiver import Receiver
from location import Location
from encryption import Encrypter

if __name__ == "__main__":
    message = "Only if we remember to turn on the light"
    location_info = [12, 13, 1]

    encrypter = Encrypter()

    sender1 = Sender(encrypter)
    encrypted_text1, key1 = sender1.encrypt([12, 13, 1], message)

    # Debug Point: print(key1)
    # Debug Point: The sender2 should return same keyhash if it lies in the location constraints
    # sender2 = Sender(encrypter)
    # encrypted_text2, key2 = sender2.encrypt([11, 12, 1], message)
    # print(key2)

    # 1. Create a Receiver using same 'encrypter' object as described above
    # 2. Pass, same key hash & same location data to the receivers decrypt method
    # 3. It should decrypt only if it lies in range