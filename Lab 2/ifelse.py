def gradepointAvg(score):
  gpa = 0
  if score>=90:
    gpa=4
  elif score>=80 and score<=89:
    gpa=3
  elif score>=70 and score<=79:
    gpa=2
  elif score>=60 and score<=69:
    gpa=1
  else:
    gpa=0
  print(gpa)
    
  
