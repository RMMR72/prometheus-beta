class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to support Kruskal's algorithm.
    
    This class provides efficient operations for tracking connected components
    and detecting cycles in a graph.
    """
    def __init__(self, vertices):
        """
        Initialize the DisjointSet with each vertex in its own set.
        
        Args:
            vertices (int or list): Number of vertices or list of vertices
        """
        if isinstance(vertices, int):
            self.parent = list(range(vertices))
            self.rank = [0] * vertices
        else:
            self.parent = {v: v for v in vertices}
            self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        """
        Find the root/representative of the set containing the item.
        Uses path compression for efficiency.
        
        Args:
            item: The item to find the set representative for
        
        Returns:
            The root/representative of the set
        """
        # Path compression
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Merge the sets containing x and y.
        Uses union by rank for efficiency.
        
        Args:
            x: First item
            y: Second item
        
        Returns:
            bool: True if union was successful (no cycle), False otherwise
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If roots are same, a cycle exists
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        # Update rank if needed
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree (MST) of a weighted, undirected graph
    using Kruskal's algorithm.
    
    Args:
        graph (list of tuples): List of edges, where each edge is 
                                (u, v, weight) format
    
    Returns:
        list: List of edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If graph is empty or None
        TypeError: If graph is not in the correct format
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Validate graph structure
    try:
        # Try to unpack first edge to check format
        u, v, weight = graph[0]
    except (ValueError, TypeError):
        raise TypeError("Graph must be a list of (u, v, weight) tuples")
    
    # Extract unique vertices
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)
    
    # Sort edges by weight
    sorted_edges = sorted(graph, key=lambda x: x[2])
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # MST will store the resulting minimum spanning tree
    mst = []
    
    # Kruskal's algorithm
    for u, v, weight in sorted_edges:
        # If adding this edge doesn't create a cycle, add it to MST
        if ds.union(u, v):
            mst.append((u, v, weight))
    
    return mst