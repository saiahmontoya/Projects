'''Creates cipher class and  creates the alphabet list. The cipher class also acts as the atbash cipher, and when it is called it reverses the alphabet list, allowing it to encrypt any message using the backwards alphabet.'''
class Cipher:

  def __init__(self):
    self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
  def encrypt_letter(self,letter):
    location = self.alphabet.rindex(letter)
    return self.alphabet[25 - location]
    

  def decrypt_letter(self,letter):
    location = self.alphabet.rindex(letter)
    return self.alphabet[25 - location]
    
      
  def encrypt_message(self,message):
    message = message.upper()
    encrypted_message = ''
    for letter in message:
      if letter.isalpha() == True:
        encrypted_letter = self.encrypt_letter(letter)
        encrypted_message = encrypted_message + encrypted_letter
      else:
        encrypted_message = encrypted_message + letter
    return encrypted_message

  def decrypt_message(self,message):
    message = message.upper()
    decrypted_message = ''
    for letter in message:
      if letter.isalpha() == True:
        decrypted_letter = self.decrypt_letter(letter)
        decrypted_message = decrypted_message + decrypted_letter
      else:
        decrypted_message = decrypted_message + letter
    return decrypted_message
        

  
    