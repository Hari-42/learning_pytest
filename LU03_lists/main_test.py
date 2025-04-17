from LU03_lists.main import simplelist, givecarbrandnames

def test_simplelist():
    result = simplelist()
    assert result == list(('Tiger', 'Lion', 'Zebra', 'Leopard'))


def test_givecarbrandnames(monkeypatch, capsys):
    inputs = iter(['BMW', 'Toyota', 'Nissan', 'Audi', 'Porsche', '3'])  # '3' as string
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    givecarbrandnames()
    captured = capsys.readouterr()

    assert "Nissan" in captured.out