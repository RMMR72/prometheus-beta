import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_initialization():
    """Test DisjointSet initialization with integers"""
    ds = DisjointSet(5)
    assert ds.parent == [0, 1, 2, 3, 4]
    assert ds.rank == [0, 0, 0, 0, 0]

def test_disjoint_set_find():
    """Test find method of DisjointSet"""
    ds = DisjointSet(5)
    assert ds.find(3) == 3
    
    # Test path compression
    ds.parent[1] = 2
    ds.parent[2] = 3
    assert ds.find(1) == 3
    assert ds.parent[1] == 3  # Path compressed
    assert ds.parent[2] == 3  # Path compressed

def test_disjoint_set_union():
    """Test union method of DisjointSet"""
    ds = DisjointSet(5)
    
    # First union should succeed
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Second union in same set should fail
    assert ds.union(0, 1) == False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph: [(u, v, weight), ...]
    graph = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 2, 8),
        (1, 7, 11),
        (2, 3, 7),
        (2, 8, 2),
        (2, 5, 4),
        (3, 4, 9),
        (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 8, 7)
    ]
    
    mst = kruskal_mst(graph)
    
    # Check total number of MST edges (should be n-1 for n vertices)
    assert len(mst) == 7 or len(mst) == 8
    
    # Calculate total MST weight
    mst_weight = sum(weight for _, _, weight in mst)
    
    # Expected MST weight should be around 37 
    assert 35 <= mst_weight <= 40
    
    # Verify no cycles
    ds = DisjointSet(set(v for edge in mst for v in edge[:2]))
    for u, v, _ in mst:
        assert ds.union(u, v) == True

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty graph"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        kruskal_mst([])

def test_kruskal_mst_invalid_graph():
    """Test Kruskal's algorithm with invalid graph format"""
    with pytest.raises(TypeError, match="Graph must be a list of"):
        kruskal_mst([(1, 2)])  # Missing weight
    
    with pytest.raises(TypeError, match="Graph must be a list of"):
        kruskal_mst("not a graph")  # Wrong type

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph"""
    graph = [
        (0, 1, 1),
        (2, 3, 2),
        (4, 5, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Each set of vertices should have one edge
    assert len(mst) == 3
    assert set((0, 1, 1)) in [set(edge) for edge in mst]
    assert set((2, 3, 2)) in [set(edge) for edge in mst]
    assert set((4, 5, 3)) in [set(edge) for edge in mst]