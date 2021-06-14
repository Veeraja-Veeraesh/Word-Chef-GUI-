import enchant
import itertools as it
import getRandomLetters as rndltr


def anagramCheck(levelNo):
  while True:
    randltrlist=rndltr.RandomLetters(levelNo)
    allAnagrams=[]

    for i in range(2,len(randltrlist)+1):
      allAnagrams+=[''.join(permutation) for permutation in it.permutations(randltrlist,i)]

    listOfAnagrams=[]
    dictengUK=enchant.Dict("en_GB")

    for word in allAnagrams:
      if dictengUK.check(word)==True and len(word)>2:
        listOfAnagrams.append(word)
    if len(set(listOfAnagrams))!=(len(listOfAnagrams)):#TO MAKE SURE WORDS ARE NOT REPEATED
      continue
    else:
      pass
      
    if len(listOfAnagrams)<4:#TO MAKE SURE ENOUGH SOLUTIONS ARE POSSIBLE
      continue
    else:
      pass
    
    if not listOfAnagrams:#TO MAKE SURE LIST IS NOT EMPTY
      continue
    else:
      break
      
    
  return (randltrlist,listOfAnagrams)#returns solution
