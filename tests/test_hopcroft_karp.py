import pytest
from src.hopcroft_karp import HopcroftKarp

def test_simple_graph():
    """Test a simple bipartite graph with a clear maximum matching."""
    graph = {
        1: [3, 4],
        2: [3, 5],
        3: [1, 2],
        4: [1],
        5: [2]
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4, 5}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # Verify the matching is valid
    assert len(matching) == 4  # 2 edges
    assert matching[1] in {3, 4}
    assert matching[2] in {3, 5}
    assert matching[3] == (1 if matching[1] == 3 else 2)
    assert matching[matching[1]] == 1
    assert matching[matching[2]] == 2

def test_complete_bipartite_graph():
    """Test a complete bipartite graph where all vertices can be matched."""
    graph = {
        1: [4, 5, 6],
        2: [4, 5, 6],
        3: [4, 5, 6],
        4: [1, 2, 3],
        5: [1, 2, 3],
        6: [1, 2, 3]
    }
    left_vertices = {1, 2, 3}
    right_vertices = {4, 5, 6}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # In a complete bipartite graph, max matching is min(|left|, |right|)
    assert len(matching) == 6  # Full matching

def test_no_matching_graph():
    """Test a graph with no possible matching."""
    graph = {
        1: [],
        2: [],
        3: []
    }
    left_vertices = {1, 2, 3}
    right_vertices = {4, 5, 6}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    assert len(matching) == 0

def test_empty_graph_raises_error():
    """Verify that empty graph or vertex sets raise an error."""
    with pytest.raises(ValueError):
        HopcroftKarp({}, set(), set())

def test_invalid_graph_structure():
    """Test that invalid graph structures raise an error."""
    with pytest.raises(ValueError):
        HopcroftKarp({1: "not a list"}, {1}, {2})

def test_single_vertex_graph():
    """Test a graph with just one vertex in each partition."""
    graph = {1: [2]}
    left_vertices = {1}
    right_vertices = {2}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    assert len(matching) == 2
    assert matching[1] == 2
    assert matching[2] == 1

def test_asymmetric_bipartite_graph():
    """Test a graph with asymmetric partitions."""
    graph = {
        1: [4],
        2: [4, 5],
        3: [5, 6],
        4: [1, 2],
        5: [2, 3],
        6: [3]
    }
    left_vertices = {1, 2, 3}
    right_vertices = {4, 5, 6}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # Verify the matching is valid and maximal
    assert len(matching) == 6  # Full matching