'''
Created on Jan 9, 2016

@author: Krish
'''
from Vertex import Vertex
from Queue import Queue


class Graph:
   
     def __init__(self):
         self.vertList={}
         self.numVertices=0
         
     def addVertex(self,key):
         self.numVertices=self.numVertices+1
         newVertex=Vertex(key)
         self.vertList[key]=newVertex
         return newVertex
     
     def getVertex(self,key):
         if key in self.vertList:
             return self.vertList[key]
         else:
             return None
         
     def __contains__(self,key):
         return (key in self.vertList)
     
     def addEdge(self,v1,v2,cost=0):
         if v1 not in self.vertList:
             v1=Vertex(v1)
         if v2 not in self.vertList:
             v2=Vertex(v2)
         self.vertList[v1].addNeighbour(self.vertList[v2],cost)
     
     def getVertices(self):
         return self.vertList.keys()
     
     def __iter__(self):
         return iter(self.vertList.values())            
     
     
     def BFS(self,start):
         start.setDistance(0)
         vertQueue= Queue()
         vertQueue.enqueue(start)
         while(vertQueue.size()>0):
             currentVert=vertQueue.dequeue()
             for nbr in currentVert.getConnections():
                 if(nbr.getColor()=="white"):
                     nbr.setColor("gray")
                     nbr.setDistance(currentVert.getDistance()+1)
                     nbr.setPred(currentVert)
                     vertQueue.enqueue(nbr)
             currentVert.setColor("black")        
             
     def traverseGraph(self,y):
         x=y
         while(x.getPred()):
             print(x.getId())
             x=x.getPred()
         print(x.getId())    
                 
             
#########################Testing###############################################

'''
g=Graph()
for i in range(6):
    g.addVertex(i)
    
print(g.vertList)         

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
     for w in v.getConnections():
         print("( %s , %s )" % (v.getId(), w.getId()))

       
g.BFS(g.getVertex(0))
g.traverseGraph(g.getVertex(3))         
'''         
        