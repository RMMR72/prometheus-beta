import heapq
from typing import Dict, List, Tuple, Union

def prims_mst(graph: Dict[str, Dict[str, int]]) -> Union[List[Tuple[str, str, int]], None]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency list 
                                           where keys are vertices and values are 
                                           dictionaries of neighboring vertices and 
                                           their edge weights.
    
    Returns:
        Union[List[Tuple[str, str, int]], None]: A list of edges in the MST, 
                                                 where each edge is a tuple 
                                                 (source, destination, weight). 
                                                 Returns None if the graph is empty 
                                                 or disconnected.
    
    Raises:
        ValueError: If the input graph is not a valid graph representation.
    """
    # Validate input
    if not graph or not isinstance(graph, dict):
        raise ValueError("Input must be a non-empty dictionary representing a graph")
    
    # If graph is empty, return None
    if len(graph) == 0:
        return None
    
    # Start with an arbitrary vertex
    start_vertex = list(graph.keys())[0]
    
    # Track visited vertices and the MST edges
    visited = set()
    mst_edges = []
    
    # Priority queue to store edges to explore
    # Format: (weight, source, destination)
    pq = []
    
    # Start exploring from the first vertex
    visited.add(start_vertex)
    
    # Add edges from the start vertex to the priority queue
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(pq, (weight, start_vertex, neighbor))
    
    # Continue until all vertices are visited or no more edges can be added
    while pq:
        # Get the minimum weight edge
        weight, src, dest = heapq.heappop(pq)
        
        # Skip if destination is already visited
        if dest in visited:
            continue
        
        # Add the edge to MST and mark destination as visited
        mst_edges.append((src, dest, weight))
        visited.add(dest)
        
        # Explore edges from the newly added vertex
        for next_neighbor, next_weight in graph[dest].items():
            if next_neighbor not in visited:
                heapq.heappush(pq, (next_weight, dest, next_neighbor))
    
    # Check if MST includes all vertices
    if len(visited) != len(graph):
        return None
    
    return mst_edges