def First100EvenSum():
  acc=0
  for x in range(0,101,2):
      acc = acc + x
  print(acc)      
      
      
def First50OddSum():
  acc=0
  for x in range(1,50,2):
    acc = acc + x
  print(acc)   
  
def First100Avg():
  acc=0
  counter=0
  average=0
  for x in range(1,100,2):
      acc = acc + x
      counter = counter + 1
  average = acc / counter
  print(average)
  
