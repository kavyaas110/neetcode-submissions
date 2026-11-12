"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        start = node
        q = [start] if start else []
        p_map = {start:None}
        clone_val_node_map = {}
        my_start = None

        while len(q) > 0:
            curr = q.pop(0)
            clone_val = curr.val
            clone_neighbors = curr.neighbors
            if clone_val not in clone_val_node_map:
                clone_curr = Node(clone_val)
            else:
                clone_curr = clone_val_node_map[clone_val]
            clone_val_node_map[clone_val] = clone_curr
            if not my_start:
                my_start = clone_curr
            for neighbor in clone_neighbors:
                if neighbor.val not in clone_val_node_map:
                    #create and add neighbor
                    clone_neighbor = Node(neighbor.val)
                    clone_val_node_map[neighbor.val] = clone_neighbor
                clone_curr.neighbors.append(clone_val_node_map[neighbor.val])
            for neighbor in clone_neighbors:
                if neighbor not in p_map:
                    q.append(neighbor)
                    p_map[neighbor] = curr
        return my_start

        
        
        