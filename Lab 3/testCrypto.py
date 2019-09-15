def encryptThrice():
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  key = "sprilgeoqmcykuhwbxvnjdtzfa "
  firstText = ""
  secondText = ""
  thirdText = ""
  msg = input("Please input message to be encrypted:")
  msg = msg.lower()  
  for ch in msg:
    idx = alphabet.find(ch)
    firstText = firstText + key[idx]
  for ch in firstText:
    idx = alphabet.find(ch)
    secondText = firstText + key[idx]
  for ch in secondText:
    idx = alphabet.find(ch)
    thirdText = secondText + key[idx]
  print("The encrypted message is" , thirdText)
  

    
