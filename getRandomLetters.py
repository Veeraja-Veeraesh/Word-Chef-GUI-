import random as rnd

def RandomLetters(levelNo):
  flag=True
  while flag:
    listOfLetters=[chr(i) for i in range(65,91)]
    randomLetters=[]
    # to stop errors and restart the code if error comes up 
    try:
      for i in range(1,levelNo+3):
        randomLetters.append(listOfLetters[rnd.randint(0,len(listOfLetters))])
       
      break
    except(IndexError):
    # print("Error encountered")   to find what will happen if error is raised
      continue# if error pops up then the loop is done once more to get accurate vlaues
  return randomLetters   #returns the question
