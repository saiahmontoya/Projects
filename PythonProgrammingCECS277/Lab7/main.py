
'''Group 13 Sebastian Rosas and Saiah Montoya
This program allows the user to input a text file and encrypt or decrypt said file, using the Caesarian cipher and the Atbash cipher encryption techniques. The program takes an input from the console, and encrypts the message into "message.txt". The program also allows the user to take the already encrypted message and decrypt it using whichever cipher that is preferred.'''

import caesar_cipher
import cipher
import check_input

def main():
  while 0 == 0:
    '''Asks user to choose encryption or decryption, and then which encryption method they would like to be used'''
    print('Secret Decoder Ring:\n1.Encrypt\n2.Decrypt\n')
    encrypt_decrypt = check_input.get_int_range('', 1, 2)
    
    print('\nEnter Encryption Type:\n1.Atbash\n2.Caesar\n')
    cipher_type = check_input.get_int_range('', 1, 2)

    if encrypt_decrypt == 1:
      message = input('\nEnter Message: ')

      if cipher_type == 1:
        cipher1 = cipher.Cipher()
      else:
        shift = check_input.get_int_range("Enter shift Value: ",0,25)
        cipher1 = caesar_cipher.Caesar_Cipher(shift)

      message = cipher1.encrypt_message(message)
      
      '''Saves message to text file'''
      
      with open('message.txt','w') as file:
        file.write(message)
        
      print('\nEncrypted message saved to message.txt\n')

    else:
      if cipher_type == 1: 
        cipher1 = cipher.Cipher()
      else: 
        shift = check_input.get_int_range('Enter shift Value: ',0,25)
        cipher1 = caesar_cipher.Caesar_Cipher(shift)

      '''Opens the encrypted message from .txt into the console'''

      print('\nReading encrypted message from message.txt\n')
      with open('message.txt') as file:
        message = file.read()

      message = cipher1.decrypt_message(message)
      print('Decrypted message: '+message+'\n')

main()

      

