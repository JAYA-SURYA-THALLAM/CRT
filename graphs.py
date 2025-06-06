class GraphList:
    def __init__(self):
        self.graph={}


    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]

            #add the node v if its not in graph
        if v not in self.graph:
            self.graph[v]=[]

            #since it is undirected graph,add each to others list
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print("adjacency list:")        
        for i in self.graph:
            print(f"  -->{self.graph[i]}")
#inserting nodes
g=GraphList()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,7)
#display the adjacency list
g.display()