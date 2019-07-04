#!/usr/bin/python

ciphertext="Qwtguhexcymwlhtzltjiwyuxethizyetcowqbpgzcwb"
if not ciphertext.isupper():
	ciphertext=ciphertext.upper()
key=raw_input('Enter the key : ')
if not key.isupper():
	key=key.upper()
plaintext=""
for character in range(len(ciphertext)):
	character=ord(ciphertext[character])-ord(key[character%len(key)]) +65
	if character<65:
		character= character+26
	plaintext=plaintext+chr(character)
print "Encrypted message : " + plaintext