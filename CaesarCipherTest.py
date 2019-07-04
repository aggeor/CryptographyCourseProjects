#!/usr/bin/python

ciphertext=raw_input('Enter the encrypted message: ')
plaintext=""
for key in range(1,26):
 plaintext=plaintext+"_%d_"%key
 for character in ciphertext:
  if character.isalpha():
    if character.isupper():
      is_uppercase=True
      character=character.lower()
    else:
      is_uppercase=False
    character=ord(character)-key
    if character<97:
      character=character+26
    character=chr(character)
    if is_uppercase:
      character=character.upper()
    plaintext=plaintext+character
  else:
    plaintext=plaintext+character
print "Encrypted message : " + plaintext