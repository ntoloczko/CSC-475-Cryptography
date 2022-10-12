import random
import time

def generateKey(string, seed):
    random.seed(seed)
    key = random.randbytes(len(string)) #unique key for the sequence
    return key

def encrypt(string, seed):
    key = generateKey(string, seed)
    encoded_string = string.encode()
    byte_array = bytearray(encoded_string)
    text_length = len(string)

    encrypted_array = []
    for i in range(0, text_length):
        encrypted_array.append((byte_array[i] ^ key[i])) #XOR's each individual byte of the key and string

    encrypted_byte = bytes(encrypted_array) #converts new byte array to a true byte
    return encrypted_byte
    

def decrypt(encrypted_string, seed):
    key = generateKey(encrypted_string, seed)
    encrypted_array = bytearray(encrypted_string)
    text_length = len(encrypted_array)

    decrypted_array = []
    for i in range(0, text_length):
        decrypted_array.append((encrypted_array[i] ^ key[i])) #XOR's theindividual bytes of the key and encrypted byte to get the original encoding

    decrypted_byte = bytes(decrypted_array).decode() #gets original string
    return decrypted_byte

def main():
    seed = int(time.time()) #unique seed for the sequence
    string = input("Please enter the string to be encoded: ")
    encrypted_byte = encrypt(string, seed)
    decrypted_byte = decrypt(encrypted_byte, seed)
    print(f"""
    Random seed: {seed} 
    Input string: {string} 
    Psuedo random sequence: {generateKey(string, seed)} 
    Output byte: {encrypted_byte} 
    Decrypted byte: {decrypted_byte}
    """)

main()