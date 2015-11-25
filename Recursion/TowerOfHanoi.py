'''
Created on Oct 10, 2015

@author: Krish
'''
import stackNew 
class TowerOfHanoi:
     def __init__(self, numDisks):
         self.numDisks = numDisks
         self.towers = [Stack(), Stack(), Stack()]
         for i in range(n, -1, -1):
             towers[0].push(i);
 
     def moveDisk(src, dest):
         towers[dest].push(towers[src].pop())
 
     def moveTower(n, src, spare, dest):
        if n == 0:
            moveDisk(src, dest)
        else:
            moveTower(n-1, src,dest, spare)
            moveDisk(src, dest)
            moveTower(n-1, spare, src, dest)