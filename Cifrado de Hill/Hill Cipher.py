import numpy as np
from sympy import Matrix
import math as mt
import random
import time

#Diccionarios para encriptar y desencriptar
encryptDictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z':26}

decryptDictionary = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', 
            '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'Ñ', '15': 'O', 
            '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
            
#Genera la matriz key aleatoriamente asegurándose de que sea inv mod 27
def GenKey(size):
    
    key = []
    temp = []

    det = 0
    mcd = 0
    isValid = False

    while(isValid == False):
        for x in range (size*size): #Generación de matriz aleatoria
            temp.append(random.randrange(27))

        key = np.array(temp).reshape(size,size)
        det = Matrix(key).det()
        mcd = mt.gcd(int(det), 27)
        if(det != 0 and mcd == 1): #Verifica que sea invertible
            isValid = True
        temp = []
    return key #retorna la matriz
        
def HillCipher(message,key):

    cipherMessage = ''
    messageVector = []
    C = []
    temp = []
    cont = 0

    message = message.upper()

    if(len(message) <= len(key)):
        while(len(message) < len(key)):
            message = message + 'X' #Rellena con X hasta que sea del mismo tamaño que la matriz
        
        for i in range(len(message)): #Se genera el vector mensaje
            messageVector.append(encryptDictionary[message[i]])

        messageVector = np.array(messageVector)
        
        #Obtiene el mensaje cifrado
        C = np.matmul(key,messageVector)
        C = C % 27
        
        for i in range(len(C)):
            cipherMessage += decryptDictionary[str(C[i])]
    else:
        #Rellena eel mensaje con X hasta que sea múltiplo del tamaño de Key
        while( len(message) % len(key) != 0 ):
            message = message + 'X'
            
        #Convierte el vector en una matriz
        messageVector = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
        
        #Recorre cada bloque y lo multiplica por key para obtener el vector cifrado
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
    D = []
    inverseK = []
    temp = []
    
    #Convierte el vector cifrado en una matriz
    cipherVector = [cmessage[i:i+len(key)] for i in range(0,len(cmessage), len(key))]
    
    #Calcula la inversa mod 27
    inverseK = Matrix(key).inv_mod(27)
    inverseK = np.array(inverseK)
    
    #Recorre cada bloque y lo multiplica por key para obtener el vector mensaje
    for bloque in cipherVector:
        for i in range(0,len(bloque)):
            temp.append(encryptDictionary[bloque[i]])
            
        temp = np.array(temp)
        
        D = np.matmul(inverseK,temp)
        D = (D % 27).flatten()
        
        for i in range(len(D)):
            decipherMessage += decryptDictionary[str(int(D[i]))]
        
        temp = []
        
    #Remueve los X añadidos al cifrar el mensaje
    while(decipherMessage[-1] == 'X'):
        decipherMessage = decipherMessage[:-1]
    
    return decipherMessage

#Ejecucion del programa    
def main():
    size = 0 
    matrix = []
    C = ""
    M = ""
    D = ""
    
    size = int(input("Ingrese el tamaño de la matriz cuadrada(key): "))
    key = GenKey(size)
    
    print("La matriz Key es: \n", key)
    M = input("Ingrese el mensaje a cifrar: ")
    C = HillCipher(M, key)
    
    print("El mensaje cifrado es: ", C)
    
    inicio = time.time()
    print("Descrifrando mensaje...")
    D = HillDecipher(C,key)
    fin = time.time()
    print("El mensaje descifrado es: ", D)
    print("Tiempo de descifrado: ", fin-inicio)

main()
    