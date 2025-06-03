class graph:
    def _init_(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:  #creating node in u variable
            self.graph[u]=[]
            
        if v not in self.graph:
            self.graph[v]=[]      #creating edge in v variable
                    
            
            
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def display(self):
        print("Adjacent list")
        for i in self.graph:
            print(f"{i}--->{self.graph[i]}")
    def bfs(self, start):
        visited = set() 
        queue=[start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex) 
                print(vertex,end=" ")
                for i in self.graph[vertex]:
                    if i not in visited:
                        queue.append(i)
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i, visited)


g=graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,7)
g.display()
g.bfs(1)
g.display()
g.dfs(1)