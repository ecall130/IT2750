#subsitution cipher

def Encrypt():
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  key = "sprilgeoqmcykuhwbxvnjdtzfa "
  cipherText = ""
  msg = input("Please input message to be encrypted:")
  msg  = msg.lower()
  for ch in msg:
    idx = alphabet.find(ch)
    cipherText = cipherText + key[idx] 
  print("The encrypted message is" , cipherText)
  
  def Decrypt():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    key = "sprilgeoqmcykuhwbxvnjdtzfa "
    cipherText = ""
    msg = input("Please input message to be decrypted:")
    msg  = msg.lower()
    for c in msg:
      idx = key.find(c)
      cipherText = cipherText + alphabet[idx]
    print("The decrypted message is" , cipherText)
    
    
  
