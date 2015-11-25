'''
Created on Nov 12, 2015

@author: Krish
'''


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
     visited, stack = set(), [start]
     while stack:
        vertex = stack.pop()
        print("current popped vertex is",vertex)
        if vertex not in visited:
            visited.add(vertex)
            print(graph[vertex] - visited)
            stack.extend(graph[vertex] - visited)
            print("stack is",stack)
            print("Visited is",visited)
     return visited
#print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'} 

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    print("Stack is",stack)
    while stack:
         #print(vertex, path)
         (vertex, path) = stack.pop()
         print(vertex, path)
         for next in graph[vertex] - set(path):
            if next == goal: 
                print(path + [next])
                yield path + [next]
            else:
                stack.append((next, path + [next])) 
                print("Stack Here is",stack)
                
print(list(dfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]                