
def getMostFrequent():
  newStr = input("Please input a sentence:")
  newStr = newStr.lower()
  newStr = list(newStr)
  spaces = newStr.count(' ')
  while spaces > 0:
    newStr.remove(' ')
    spaces = newStr.count(' ')
  from statistics import mode
  print(mode(newStr))
  
  
def uniqueLetters():
  newStr = input("Please input a sentence:")
  newStr = newStr.lower()
  newStr = list(newStr)
  newStr.sort()
  countlist = [ ]
  previous = newStr[0]
  grpCount = 0
  for current in newStr:
    if current == previous:
      grpCount = grpCount + 1
      previous = current
    else:
      print(previous, "  ", grpCount)
      previous = current
      grpCount = 1
  print(current, "  ", grpCount)


  
