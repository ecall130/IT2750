# Problem 7.1

x = 0
while x < 50:
  x = x + 5
  print(x)
  
# Problem 7.2

x = input("Please input a sentence:")
x = list(x)
spaces = x.count(' ')
counter = 0
while spaces > 0:
  spaces = spaces - 1
  counter = counter + 1
print("The number of spaces in the sentence is",counter,".")

# Problem 7.3

counter = 0
x = 0
examScore = ' '
while examScore !=  "Stop":
  examScore = ("Please enter exam score:")
  if examScore != "Stop" and examScore.isdigit()
    x = x +int(examScore)
    counter = counter + 1
  else:
    break
print("The average of the scores is:",x/counter)

# Problem 7.4

x = input("Please input a word:")
x = list(x)
if x == x[len(x)::-1]:
  print("True")
else:
  print("False")
    
