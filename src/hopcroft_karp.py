from typing import Dict, List, Optional, Set

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in bipartite graphs.
    
    The algorithm finds the maximum matching in a bipartite graph efficiently 
    with a time complexity of O(E * sqrt(V)).
    
    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the bipartite graph
        left_vertices (Set[int]): Set of vertices in the left partition
        right_vertices (Set[int]): Set of vertices in the right partition
    """
    
    def __init__(self, graph: Dict[int, List[int]], left_vertices: Set[int], right_vertices: Set[int]):
        """
        Initialize the Hopcroft-Karp algorithm.
        
        Args:
            graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
            left_vertices (Set[int]): Vertices in the left partition
            right_vertices (Set[int]): Vertices in the right partition
        
        Raises:
            ValueError: If the graph is not bipartite or inputs are invalid
        """
        # Validate inputs
        if not graph or not left_vertices or not right_vertices:
            raise ValueError("Graph and vertex sets cannot be empty")
        
        # Verify graph structure
        for vertex in graph:
            if not isinstance(graph[vertex], list):
                raise ValueError(f"Adjacency list for {vertex} must be a list")
        
        self.graph = graph
        self.left_vertices = left_vertices
        self.right_vertices = right_vertices
        
        # Key data structures for the algorithm
        self.matching = {}  # Matched partners for vertices
        self.dist = {}      # Distance labels for BFS
    
    def bfs(self) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        queue = []
        
        # Initialize distances for left vertices
        for u in self.left_vertices:
            if self.matching.get(u) is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        # Sentinel to mark end of level
        self.dist[None] = float('inf')
        
        # BFS to find shortest augmenting paths
        while queue:
            u = queue.pop(0)
            
            if self.dist[u] < self.dist[None]:
                for v in self.graph.get(u, []):
                    # Follow unmatched or alternating edges
                    matched_to_w = self.matching.get(v)
                    
                    if self.dist.get(matched_to_w, float('inf')) == float('inf'):
                        if matched_to_w is None:
                            return True  # Found augmenting path
                        
                        # Extend the search
                        self.dist[matched_to_w] = self.dist[u] + 1
                        queue.append(matched_to_w)
        
        return False
    
    def dfs(self, u: Optional[int]) -> bool:
        """
        Depth-first search to find and extend augmenting paths.
        
        Args:
            u (Optional[int]): Current vertex in the search
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        if u is None:
            return True
        
        for v in self.graph.get(u, []):
            # Check if this is a promising edge in an augmenting path
            matched_to_w = self.matching.get(v)
            
            if (self.dist.get(matched_to_w, float('inf')) == self.dist[u] + 1 and 
                self.dfs(matched_to_w)):
                # Extend the matching
                self.matching[v] = u
                self.matching[u] = v
                return True
        
        # No augmenting path found
        self.dist[u] = float('inf')
        return False
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Compute the maximum matching in the bipartite graph.
        
        Returns:
            Dict[int, int]: A dictionary of matched vertex pairs
        """
        # Reset matching
        self.matching.clear()
        
        # Continue finding augmenting paths
        while self.bfs():
            for u in self.left_vertices:
                if self.matching.get(u) is None:
                    self.dfs(u)
        
        return self.matching