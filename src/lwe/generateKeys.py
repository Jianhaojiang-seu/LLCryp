import random

class Keys:
    def generatePublicKeys(self, secrectKey):
        n = 20 # number of values in public key A and B
        B=[]
        e=[]

        s = secrectKey
        q=97 # modulo number
        A = random.sample(range(q), n)
        for x in range(0,len(A)):
            e.append(random.randint(1,4))
            B.append((A[x]*s + e[x]) % q)

        return (A, B, q)


