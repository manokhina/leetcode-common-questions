"""
Question:
Clone an undirected graph. Each node in the graph contains a label and
a list of its neighbors.
"""


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(v):
            u = UndirectedGraphNode(v.val, [])
            visited[v] = u
            for ngh in v.neighbors:
                if ngh not in visited:
                    u.neighbors.append(dfs(ngh))
                else:
                    u.neighbors.append(visited[ngh])
            return u

        visited = {}
        return dfs(node)
