import pytest
from src.tower_of_hanoi import solve_tower_of_hanoi

def test_zero_disks():
    """Test solving Tower of Hanoi with 0 disks"""
    moves = solve_tower_of_hanoi(0)
    assert moves == [], "No moves should be made for 0 disks"

def test_one_disk():
    """Test solving Tower of Hanoi with 1 disk"""
    moves = solve_tower_of_hanoi(1)
    assert moves == [('A', 'C')], "Single disk should move directly from A to C"
    assert len(moves) == 1, "Should have exactly one move for 1 disk"

def test_two_disks():
    """Test solving Tower of Hanoi with 2 disks"""
    moves = solve_tower_of_hanoi(2)
    expected_moves = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    assert moves == expected_moves, "Incorrect move sequence for 2 disks"
    assert len(moves) == 3, "Should have exactly 3 moves for 2 disks"

def test_three_disks():
    """Test solving Tower of Hanoi with 3 disks"""
    moves = solve_tower_of_hanoi(3)
    assert len(moves) == 7, "Should have exactly 7 moves for 3 disks"

def test_seven_disks():
    """Test solving Tower of Hanoi with 7 disks"""
    moves = solve_tower_of_hanoi(7)
    assert len(moves) == 127, "Should have exactly 127 moves for 7 disks"

def test_custom_rod_names():
    """Test solving Tower of Hanoi with custom rod names"""
    moves = solve_tower_of_hanoi(2, source_rod='X', auxiliary_rod='Y', destination_rod='Z')
    expected_moves = [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
    assert moves == expected_moves, "Should work with custom rod names"

def test_negative_disks():
    """Test that negative number of disks raises a ValueError"""
    with pytest.raises(ValueError, match="Number of disks must be non-negative"):
        solve_tower_of_hanoi(-1)

def test_moves_count_formula():
    """Verify that the number of moves follows 2^n - 1 formula"""
    for n in range(8):  # Test for 0 to 7 disks
        moves = solve_tower_of_hanoi(n)
        assert len(moves) == (2**n - 1), f"Incorrect number of moves for {n} disks"