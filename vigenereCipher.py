import pathlib
from random import *
from string import ascii_letters

# Key Generator
def generateKey(n):
    is_int = False
    while is_int is False:
        try:
            key = ""
            alphabet = list(ascii_letters) #should establish the elements that can form the random key
            for num in range (n): #create the key to fit the desired size
                alphabet_index = int(random()*len(alphabet))
                key += alphabet[alphabet_index]
            is_int = True
        except ValueError:
            n = input("Error! Please enter an integer: ")
    
    return key #return the newly made key

# Encryption Function
def encrypt(file_path, key_file):
    found = False
    while not found: #while the file path has not produced a file
        try:
            encrypting_file = pathlib.Path(file_path)
            file = open(encrypting_file)
            file.close()
            found = True
        except FileNotFoundError:
            file_path = input("Error! Please enter a valid path to the file: ")
    
    keyFile = open(key_file, 'r') #obtains the key for use in encryption
    key = keyFile.readline()
    keyFile.close()
    
    file = open(encrypting_file, "r+") #allows for reading and writing

    file_lines = [] #stores all of the encrypted letters and other miscellaneous characters to be placed into the new file
    i = 0

    for line in file:
        for letter in line:
            if (ord(letter) not in range(65, 91) and ord(letter) not in range(97, 123)): #when the character is not alphabetic
                file_lines.append(letter)
                continue
            else:
                if ord(letter) < 91: #for the uppercase letters
                    new_ascii = ((ord(key[i].upper()) - 
                    ord('A')) + (ord(letter) - ord('A')))%26
                    letter = chr(new_ascii + ord('A'))
                    file_lines.append(letter)
                else: #for the lowercase letters
                    new_ascii = ((ord(key[i].lower()) - 
                    ord('a')) + (ord(letter) - ord('a')))%26
                    letter = chr(new_ascii + ord('a'))
                    file_lines.append(letter)

                i += 1
                if i >= len(key): #resets the letter of the key that is being compared when it has gone through a
                    i = 0         #full iteration

    file.close()
    append_index = file.name.index(".") #adds _end to the end of the file name
    new_file_name = file.name[:append_index] + "_end" + file.name[append_index:]

    encrypted_file = open(new_file_name, "w")
    for element in file_lines:
        encrypted_file.write(element)
    
    encrypted_file.close()
     
#Decryption Function
def decrypt(file_path, key_file):
    found = False
    while not found: #while the file path has not produced a file
        try:
            decrypting_file = pathlib.Path(file_path)
            file = open(decrypting_file)
            file.close()
            found = True
        except FileNotFoundError:
            file_path = input("Error! Please enter a valid path to the file: ")
    
    keyFile = open(key_file, 'r') #obtains the key for use in decryption
    key = keyFile.readline()
    keyFile.close()
    
    file = open(decrypting_file, "r+")

    file_lines = [] #stores the characters of the file
    i = 0

    for line in file:
        for letter in line:
            if (ord(letter) not in range(65, 91) and ord(letter) not in range(97, 123)): #if the character is not alphabetic
                file_lines.append(letter)
                continue
            else:
                if ord(letter) < 91: #for uppercase letters
                    new_ascii = ((ord(letter) - ord('a') -
                     (ord(key[i].upper()) - 
                    ord('a'))))%26
                    letter = chr(new_ascii + ord('A'))
                    file_lines.append(letter)
                else: #for lowercase letters
                    new_ascii = ((ord(letter) - ord('a') -
                     (ord(key[i].lower()) - 
                    ord('a'))))%26
                    letter = chr(new_ascii + ord('a'))
                    file_lines.append(letter)

                i += 1
                if i >= len(key): #resets the letter of the key being used if it has iterated through it
                    i = 0

    file.close()
    new_file_name = file.name.replace("_end", "_dec") #adds the _dec title to the name of the file

    encrypted_file = open(new_file_name, "w")
    for element in file_lines: #writes all the lines back to the file
        encrypted_file.write(element)
    
    encrypted_file.close()

#driver function
def main():
    key_size = int(input("Please enter the size of the key to be generated: "))
    key = generateKey(key_size)
    key_filename = input("Please enter the name of the file which will store the key (end with '.txt'): ")
    key_file = open(key_filename, "w")
    key_file.write(key)
    key_file.close()
    
    file_path = input("Please enter the path to the file you wish to encrypt: ")
    encrypt(file_path, key_filename)
    file_path = input("Please enter the path to the file you wish to decrypt: ")
    decrypt(file_path, key_filename)

main()