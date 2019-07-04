#!/usr/bin/python

import string

alphabet = string.ascii_uppercase
plaintext = raw_input('Enter the message : ')
ciphertext = ""	
InversekeyA=1
for keyB in range(1,len(alphabet)):
	ciphertext = ciphertext + "___%d___" %(keyB)
	for keyA in range(1,len(alphabet),2):
		ciphertext = ciphertext + "_%d_" %(keyA)
		for i in range(0,len(alphabet)):
			checker=(keyA*i)%26
			if checker==1:
				InversekeyA=i
		for character in plaintext:
			if character in alphabet:
				character = alphabet.find(character)
				ciphertext = ciphertext + alphabet[((character - keyB)*(InversekeyA)) % len(alphabet)]
			else:
				ciphertext = ciphertext + character
print"Encrypted message : " + ciphertext
