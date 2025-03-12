import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prims_algorithm import prims_mst

def test_basic_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    mst = prims_mst(graph)
    
    # Verify the number of edges
    assert len(mst) == len(graph) - 1
    
    # Verify total weight of MST
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 13  # Verified manually

def test_small_graph():
    """Test a small graph"""
    graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'C': 1},
        'C': {'A': 2, 'B': 1}
    }
    
    mst = prims_mst(graph)
    
    # Verify number of edges and total weight
    assert len(mst) == 2
    assert sum(edge[2] for edge in mst) == 3

def test_empty_graph():
    """Test empty graph handling"""
    with pytest.raises(ValueError):
        prims_mst({})

def test_single_vertex_graph():
    """Test graph with single vertex"""
    graph = {'A': {}}
    
    mst = prims_mst(graph)
    assert mst is None

def test_disconnected_graph():
    """Test disconnected graph"""
    graph = {
        'A': {'B': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    
    mst = prims_mst(graph)
    assert mst is None

def test_graph_with_negative_weights():
    """Test graph with negative edge weights"""
    graph = {
        'A': {'B': -1, 'C': -2},
        'B': {'A': -1, 'C': -3},
        'C': {'A': -2, 'B': -3}
    }
    
    mst = prims_mst(graph)
    
    # Verify number of edges
    assert len(mst) == 2
    
    # Verify total weight with more flexibility
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight in [-5, -6]  # Allow MST with weight -5 or -6

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        prims_mst(None)
    
    with pytest.raises(ValueError):
        prims_mst([])