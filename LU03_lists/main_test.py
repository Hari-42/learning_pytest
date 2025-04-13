from LU03_lists.main import simplelist

def test_simplelist():
    result = simplelist()
    assert result == list(('Tiger', 'Lion', 'Zebra', 'Leopard'))