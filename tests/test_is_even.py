from src.is_even import is_even

def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)

def test_is_even_edge_cases():
    import sys
    assert not is_even(sys.maxsize)
    assert is_even(-2)
