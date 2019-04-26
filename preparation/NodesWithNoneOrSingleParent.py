from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v):
        visited = [False] * len(self.graph)
        self.dfsUtil(v, visited)

    def dfsUtil(self, v, visited):
        visited[v] = True

        print(v)

        for i in self.graph[v]:
            if not visited[i]:
                self.dfsUtil(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)
