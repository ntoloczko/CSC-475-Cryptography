import os
import base64


def setEnvVar():
    os.environ['VAULT_ADDR'] = 'http://127.0.0.1:8200' # Write Vault Address from server here
    os.environ['VAULT_TOKEN'] = '' # Write Vault Token from server here


def enableTransitEngine():
    os.system('vault secrets enable transit')


def createKey():
    key = '' # Write the name of the key here
    os.system(f'vault write transit/keys/{key} type=aes256-gcm96')


def decodeMessage(cipher, key):
    os.system(f'vault write transit/decrypt/{key} ciphertext={cipher}')


def encryptMessage(plain, key):
    plain = base64.b64encode(plain.encode())
    os.system(f'vault write transit/encrypt/{key} plaintext={plain.decode()}')
   

setEnvVar()
enableTransitEngine()
key = createKey()
encryptMessage('', key) # Write in the message that is being encrypted
decodeMessage('', key) # Write in the outputted ciphertext
decodedPlaintext = base64.b64decode('') # Write in the outputted plaintext
print(decodedPlaintext.decode())