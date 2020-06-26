import sys
from location import Location
from encryption import encrypt

class Sender:
    """Represents sender, contains functions to encrypt the message    
    """

    def encrypt(self, location_info, raw_message):
        """Encrypts the raw_message

        Args:
            raw_message (str): Raw un-encrytped message 

        Returns:B   
            string: a list of strings used that are the header columns
        """
        longitude, latitude, tolerance = location_info[0], location_info[1], location_info[2]
        location = Location(longitude, latitude, tolerance)
        transformed_location = location.getTransformedLocation()
        # Debug Point:
        # print(transformed_location, sys.getsizeof(transformed_location))
        encrypted_text = encrypt(transformed_location, raw_message)
        return encrypted_text

if __name__ == "__main__":
    sender = Sender();
    encrypted_text = sender.encrypt([12, 12, 1], "How you doing?")
    print(encrypted_text)
