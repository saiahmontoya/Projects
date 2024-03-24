import cipher
'''Caesar Cipher class allows user to encrypt message by shifting the alphabet list by 3 letters. '''
class Caesar_Cipher(cipher.Cipher):
  def __init__(self,shift):
    super().__init__()
    if type(shift) != type(1):
      raise ValueError('shift must be an integer')
    else:
      self.shift = shift

  def encrypt_letter(self,letter):
    location = self.alphabet.rindex(letter)
    encrypted_letter = location + self.shift
    if encrypted_letter > 25:
      encrypted_letter -= 26
    return self.alphabet[encrypted_letter]

  def decrypt_letter(self,letter):
    location = self.alphabet.rindex(letter)
    decrypted_letter = location - self.shift
    if decrypted_letter < 0:
      decrypted_letter += 26
    return self.alphabet[decrypted_letter]
    
    
  
  