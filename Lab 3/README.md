Describe the 3 simple algorithms for encryption that we covered in this lesson (it can be in 2 or 3 sentences

The chapter starts off by discussing strings, string operators, and string methods. Then is discusses encryption and several different ciphers that can be used for encryption.

3 basic string methods are:
astring.lower()  This returns a string in lowercase.
astring.replace(old,new)  This replaces the old string with the new string in a larger string.
astring.count(item)  This returns a count of the number of times the item occurs in a string.

The 3 algorithms for encryption covered by this chapter are substitution cipher, transposition cipher, and the Vignère cipher.
Substitution cipher swaps one letter for another to produce a ciphertext, this cipher allows for the creation and sharing of a key for decryption. Transposition cipher separates letters based on which are even and which are odd, forming a new string each of even and odd. The Vignère cipher is a more complex form of the subsitution cipher. It uses the Vignère square which is a table that provides a different key for each letter, from there a key word can be chosen and layered over the text to be encrypted. 

def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText 
  
 
 The above is an example of substitution cipher.
  
  
  def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  return cipherText 
  
  The above is an example of transposition cipher.
