'''
Created on Jan 9, 2016

@author: Krish
'''
import sys
import os
import unittest

class Vertex(object):
     def __init__(self,key):
         self.id=key
         self.connectedTo={}
         self.color='white'
         self.distance=sys.maxsize
         self.pred=None
         self.discovery=0
         self.finish=0
         
     def addNeighbour(self,v,weight=0): #V is vertex Object
         self.connectedTo[v]=weight
          
     def getConnections(self):
         return self.connectedTo.keys()
     
     def getId(self):
         return self.id
     
     def getWeight(self,v): #V is vertex Object
         return self.connectedTo[v]
     
     def __str__(self):
         return str(self.id) + 'connectedTo: ' +  str([x.id for x in self.connectedTo])     
     
     def setColor(self,color):
         self.color=color
         
     def setDistance(self,dist):
         self.distance=dist
         
     def setPred(self,p):
         self.pred=p          
     
     def setDiscoveryTime(self,dt):
         self.discovery=dt
     
     
     def setFinishTime(self,ft):
         self.finish-ft 
         
     def getColor(self):
         return self.color
     
     def getDistance(self):
         return self.distance 
     
     def getPred(self):
         return self.pred
     
     def getDiscoveryTime(self):
         return self.discovery
     
     def getFinishTime(self):
         return self.getFinishTime()         
     