#  File: Poker.py
# https://github.com/annaymj/Python-Code/blob/master/Poker.py

#  Description:In this program, it returns the kind of hands (e.g. full house, straight flush, et al.), and calculate the total score of each hand

#  Student's Name: Mengjie Yu

#  Student's UT EID: my3852

#  Course Name: CS 313E 

#  Unique Number: 53260

#  Date Created: 1/31/2013

#  Date Last Modified:2/1/2013

import string, math, random

from poker import Poker

def main ():
  numHands = eval (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = eval( input ('Enter number of hands to play: ') )
  game = Poker (numHands)
  game.play()  

  print('\n')
  for i in range(numHands):
    curHand=game.hands[i]
    print ("Hand "+ str(i+1) + ": " , end="")
    game.isRoyal(curHand)

  maxpoint=max(game.tlist)
  maxindex=game.tlist.index(maxpoint)

  print ('\nHand %d wins'% (maxindex+1))
  
main()


