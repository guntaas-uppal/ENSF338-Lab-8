class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        """Creates a new node with the given data and adds it to the graph"""
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
        return GraphNode(data)

    def removeNode(self, node):
        """Removes the node from the graph"""
        if node.data in self.adjacency_list:
            del self.adjacency_list[node.data]
            for edges in self.adjacency_list.values():
                edges[:] = [edge for edge in edges if edge[0] != node.data]

    def addEdge(self, n1, n2, weight=1):
        """Creates an edge between nodes n1 and n2 with the given weight"""
        if n1.data in self.adjacency_list and n2.data in self.adjacency_list:
            self.adjacency_list[n1.data].append((n2.data, weight))
            self.adjacency_list[n2.data].append((n1.data, weight))

    def removeEdge(self, n1, n2):
        """Removes the edge between nodes n1 and n2"""
        self.adjacency_list[n1.data] = [edge for edge in self.adjacency_list[n1.data] if edge[0] != n2.data]
        self.adjacency_list[n2.data] = [edge for edge in self.adjacency_list[n2.data] if edge[0] != n1.data]

    def importFromFile(self, file_path):
        """Imports a graph from a file using a simplified GraphViz format"""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if not lines[0].strip().startswith('strict graph'):
                    return None
                self.adjacency_list.clear()
                for line in lines[1:]:
                    if '--' in line:
                        parts = line.split('--')
                        n1_data = parts[0].strip()
                        n2_data, _, attributes = parts[1].partition('[')
                        n2_data = n2_data.strip()
                        weight = 1
                        if '[' in line:
                            attributes = attributes.rstrip('];\n').strip()
                            if 'weight=' in attributes:
                                weight = int(attributes.split('=')[1])
                        n1 = self.addNode(n1_data)
                        n2 = self.addNode(n2_data)
                        self.addEdge(n1, n2, weight)
        except Exception as e:
            print(f"Error importing from file: {e}")
            return None

    def printGraph(self):
        """Prints the graph's adjacency list for visualization"""
        for node, edges in self.adjacency_list.items():
            print(f"{node}: {edges}")

if __name__ == "__main__":
    graph = Graph()
    graph.importFromFile("random.dot")
    graph.printGraph()
