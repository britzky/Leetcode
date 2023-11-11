class Graph(object):

    def __init__(self, n, edges):
        # Adjacency list to represent the graph
        self.adjacencyList = [[] for _ in range(n)]
        # Constructor to initialize the graph with nodes and edges
        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge):
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))
        
    def shortestPath(self, node1, node2):
        return self.dijkstra(node1, node2)
    
    # Dijkstra's algorithm to find the shortest path
    def dijkstra(self, start, end):
        n = len(self.adjacencyList)
        distances = [float('inf')] * n
        distances[start] = 0

        # Priority queue to efficiently retrieve the node with the minimum distance
        priorityQueue = [(0, start)]

        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)

            # Skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue
            
            # If the target node is found then return the cost
            if currentNode == end:
                return currentCost

            # Explore neighbors and update distances
            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]

                # Update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))
        # Return the minimum distance of -1 if no path exists
        return -1 if distances[end] == float('inf') else distances[end]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)