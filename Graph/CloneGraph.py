import copy


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    oldToNew = {}

    def dfsClone(node):
        if node in oldToNew:
            return oldToNew[node]

        node_copy = Node(node.val)
        oldToNew[node] = node_copy

        for neighbor in node.neighbors:
            node_copy.neighbors.append(dfsClone(neighbor))

        return node_copy

    if node:
        return dfsClone(node)
    else:
        return None


