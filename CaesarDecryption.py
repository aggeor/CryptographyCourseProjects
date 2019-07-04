#!/usr/bin/python


ciphertext=" S DGFy LAEw syG, AF s ysDsPQ xsJ, xsJ sOsQ aL AK s HwJAGv Gx uANAD OsJ jwtwD KHsuwKzAHK, KLJACAFy xJGE s zAvvwF tsKw zsNw OGF LzwAJ xAJKL NAuLGJQ sysAFKL Lzw wNAD YsDsuLAu WEHAJw VMJAFy Lzw tsLLDw, JwtwD KHAwK EsFsywv LG KLwsD KwuJwL HDsFK LG Lzw WEHAJw K MDLAEsLw OwsHGF Lzw VWSlZ klSj sF sJEGJwv KHsuw KLsLAGF OALz wFGMyz HGOwJ LG vwKLJGQ sF wFLAJw HDsFwL hMJKMwv tQ Lzw WEHAJw K KAFAKLwJ sywFLK hJAFuwKK dwAs JsuwK zGEw stGsJv zwJ KLsJKzAH uMKLGvAsF Gx Lzw KLGDwF HDsFK LzsL usF KsNw zwJ HwGHDw sFv JwKLGJw xJwwvGE LG Lzw ysDsPQ "
key = 18
plaintext=""
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
print "Dencrypted message : " + plaintext