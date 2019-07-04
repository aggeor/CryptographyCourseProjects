#!/usr/bin/python

import string

alphabet = string.ascii_uppercase
ciphertext = "Hflyy Lqtuw jel hfy Yxdyt-mqtuw stnyl hfy wmk, Wydyt jel hfy Noglj-xelnw qt hfyql fgxxw ej whety, Tqty jel Ielhgx Iyt neeiyn he nqy, Ety jel hfy Nglm Xeln et fqw nglm hflety Qt hfy Xgtn ej Ielnel ofyly hfy Wfgneow xqy. Ety Lqtu he lsxy hfyi gxx, Ety Lqtu he jqtn hfyi, Ety Lqtu he rlqtu hfyi gxx gtn qt hfy nglmtyww rqtn hfyi Qt hfy Xgtn ej Ielnel ofyly hfy Wfgneow xqy."
keyA = 11
keyB = 6
plaintext = ""
for i in range(0,len(alphabet)):
	checker=(keyA*i)%26
	if checker==1:
		InversekeyA=i
print InversekeyA		
for character in ciphertext:
	if character.islower():
		is_lowercase = True
		character=character.upper()
	else:
		is_uppercase=False
	
	if character in alphabet:
		character = alphabet.find(character)
		plaintext = plaintext + alphabet[((character - keyB)*(InversekeyA)) % len(alphabet)]
	else:
		plaintext = plaintext + character
print"Encrypted message : " + plaintext
