'''
Created on Jan 11, 2016

@author: Krish
'''
from Graph import Graph
from Vertex import Vertex

class DFSGraph(Graph):
     def __init__(self):
         super().__init__()
         self.time=0
     
     def DFS(self):
         for aVertex in self:
             self.setColor("white")
             self.setPred(-1) 
         for aVertex in self:
             if aVertex.getColor()=="white":
                 self.dfsVisit(aVertex)
      
     def dfsVisit(self,startVertex):
         startVertex.setColor("gray")
         self.time=self.time + 1
         startVertex.setDiscoveryTime(self.time)
         for nextVertex in startVertex.getConnections():
             if(nextVertex.getColor()=="white"):
                 nextVertex.setPred(startVertex) 
                 self.dfsVisit(nextVertex)
         startVertex.setColor("black")
         self.time=self.time +1
         startVertex.setFinishTime(self.time)                         
         
     def isPath(self,start,end):
         self.dfsVisit(start)
         return self._pathSearch(start,end)
     
     def _pathSearch(self,start,end):
         print("Searching Predecessors from",end.getId(),"to",start.getId())
         while(end !=None):
             print(end.getId())
             if(end.getId()==start.getId()):
                 return True
             end=end.getPred()
         return False        
####################################Testing#####################################
g=DFSGraph()
for i in range(6):
    g.addVertex(i)
    
print(g.vertList)         

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(5,3,3)
g.addEdge(0,4,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
'''
for v in g:
     for w in v.getConnections():
         print("( %s , %s )" % (v.getId(), w.getId())) 
'''             
         
print(g.isPath(g.getVertex(2) ,g.getVertex(5)))         