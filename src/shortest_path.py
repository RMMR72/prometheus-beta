from collections import deque
from typing import Dict, List, Optional, Set

def find_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using Breadth-First Search.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
        start (int): Starting node.
        end (int): Destination node.
    
    Returns:
        Optional[List[int]]: Shortest path from start to end, or None if no path exists.
    
    Raises:
        ValueError: If start or end nodes are not in the graph.
    """
    # Validate input nodes exist in the graph
    if start not in graph or end not in graph:
        raise ValueError("Start or end node not in graph")
    
    # Handle case where start and end are the same
    if start == end:
        return [start]
    
    # Queue for BFS traversal
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent cycles
    visited: Set[int] = set([start])
    
    # BFS traversal
    while queue:
        current_node, path = queue.popleft()
        
        # Check neighbors
        for neighbor in graph.get(current_node, []):
            # Skip already visited nodes
            if neighbor in visited:
                continue
            
            # Create new path to neighbor
            new_path = path + [neighbor]
            
            # Check if we've reached the destination
            if neighbor == end:
                return new_path
            
            # Mark as visited and add to queue
            visited.add(neighbor)
            queue.append((neighbor, new_path))
    
    # No path found
    return None