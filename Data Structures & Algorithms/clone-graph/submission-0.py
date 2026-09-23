"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hashmap to store adjacency List
        # dfs to recursively go through all of the values
        hashMap = {}

        def dfs(node):
            # base case. if node has already been cloned or visited
            if node in hashMap:
                return hashMap[node]
            
            copy = Node(node.val)
            hashMap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
