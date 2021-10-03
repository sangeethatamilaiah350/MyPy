"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return node
        arr={}
        def dfs(node):
            if node in arr:
                return arr[node]
            else:
                new=Node(node.val)
                arr[node]=new
                for i in node.neighbors:
                    new.neighbors.append(dfs(i))
                return new
        return dfs(node)
            
        
        
