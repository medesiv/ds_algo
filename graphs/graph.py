class Graph:
    adj_list=[]
    v = 0
    def __init__(self,size):
        self.v = size
        self.adj_list = [[] for i in range(size)]
        # always use list comprehension for list of list wrong way to create would be [[]]*size

    def add_edge(self,start,end,bi_dir=True):
        a = self.adj_list[start]
        a.append(end)
        if bi_dir == True:
            b = self.adj_list[end]
            b.append(start)

    def has_eulerian_cycle(self):
        odd= 0
        for vertex in range(len(self.adj_list)):
            if(len(self.adj_list[vertex])%2==1):
                odd+=1
        # No of vertices with odd degree are 0 indicates eulerian cycle
        if odd==0:
            return True
        else:
            return False

    def has_eulerian_path(self):
        odd=0
        for vertices in range(len(self.adj_list)):
            if len(self.adj_list[vertices])%2==1:
                odd+=1
        # No of vertices with odd degree are 0 or exactly 2 indicates eulerian path
        if odd == 0 or odd ==2:
            return True
        else:
            return False

    def print_graph(self):
        for i,item in enumerate(self.adj_list):
            print(i,"->",item)

    pass

g = Graph(10)
g.add_edge(0,1)
g.add_edge(0,6)

g.add_edge(1,4)


g.add_edge(2,4)
g.add_edge(2,6)
g.add_edge(3,4)
g.add_edge(3,5)

g.add_edge(4,5)



print(g.has_eulerian_cycle())
g.print_graph()
