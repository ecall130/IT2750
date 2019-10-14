# Exercise 8.9
#    i. You do not need to check cases where the number of rails is greater than the message length divided by two because past that point you would end up with rails that have a single letter in them. This weakens the encryption and creates something easier to solve as larger and larger chunks of the message are left unencrypted as further rails are added, since this defeats the purpose the person encrypting the message wouldn't use that many rails.
#    ii. You only need to check cases where the number of rails evenly divides the total message length because the uneven division means there are blank spots in the table that the encryption program is expecting to have a value as it runs through the encryption process. If the program simply ignored those blank spots and moved onto the next value then the message would not be decryptable later due to the decryption program expecting the letters to have a different table value. If using a number of rails that does not divide equally in then the user would have to enter junk data at the end of the message in order to fill the table neatly, this is not preferable so it is much more likely they'd use a number of rails that divide evenly.

# Exercise 8.14
def wordPop(ranStr, n):
  sepWords = ranStr.split()
  nWords = []
  for word in sepWords:
    if(len(word) >= n):
      nWords.append(word)
  print(sorted(nWords))    
  
  
 # Exercise 8.18
 def endIng():
  sampleStr = input("Please enter a sentence:")
  sampleStr = sampleStr.split()
  for x in sampleStr:
    if x.endswith("ing"):
      print(x)

# Exercise 8.20
def startEnd():
  sampleStr = input("Please enter a sentence:")
  sampleStr = sampleStr.split()
  for x in sampleStr:
  if x.endswith("a") and x.startswith("a"):
    print(x)
