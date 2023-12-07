import numpy as np
import math as mt
import random
from sympy import Matrix

encryptDictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z':26}

decryptDictionary = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', 
            '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'Ñ', '15': 'O', 
            '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}

def GenKey(size):
    
    key = []
    temp = []

    det = 0
    mcd = 0
    isValid = False

    while(isValid == False):
        for x in range (size*size):
            temp.append(random.randrange(27))

        key = np.array(temp).reshape(size,size)
        det = int(np.linalg.det(key))
        mcd = mt.gcd(int(det), 27)
        if(det != 0 and mcd == 1):
            isValid = True
        temp = []
    return key
        
def HillCipher(message,key):

    cipherMessage = ''
    messageVector = []
    C = []
    temp = []
    cont = 0

    message = message.upper()

    if(len(message) <= len(key)):
        while(len(message) < len(key)):
            message = message + 'X'
        
        for i in range(len(message)):
            messageVector.append(encryptDictionary[message[i]])

        messageVector = np.array(messageVector)

        C = np.matmul(key,messageVector)
        C = C % 27

        for i in range(len(C)):
            cipherMessage += decryptDictionary[str(C[i])]
    else:
        while( len(message) % len(key) != 0 ):
            message = message + 'X'

        messageVector = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

        for bloque in messageVector:

            for i in range(len(bloque)):
                temp.append(encryptDictionary[bloque[i]])
            temp = np.array(temp)

            C = np.matmul(key, temp)
            C = C % 27

            for i in range(len(C)):
                cipherMessage += decryptDictionary[str(C[i])]
            temp = []


    return cipherMessage
        
def HillDecipher(cmessage, key):
    decipherMessage = ''
    cipherVector = []
    inverseK = []

matrix = GenKey(4)
print(HillCipher("Voya",matrix))
print(HillCipher("JalarDiscreta", matrix))
print(HillCipher("VoyaJalarDiscreta",matrix))


    