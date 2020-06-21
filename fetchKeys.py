from receiver import Receiver
def fetchPublicKeys():
        """
            We will fetch public keys of LWE( Learning With Errors) from the server. For now we'll be using dummy keys
        """
        A, B, q = Receiver().generatePublicKeys()
        return (A, B, q)