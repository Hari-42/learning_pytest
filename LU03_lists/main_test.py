from LU03_lists.main import simplelist, givecarbrandnames, add_countries, remove_countries, find_countries, loop_countries, sort_countries

def test_simplelist():
    result = simplelist()
    assert result == list(('Tiger', 'Lion', 'Zebra', 'Leopard'))


def test_givecarbrandnames(monkeypatch, capsys):
    inputs = iter(['BMW', 'Toyota', 'Nissan', 'Audi', 'Porsche', '3'])  # '3' as string
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    givecarbrandnames()
    captured = capsys.readouterr()

    assert "Nissan" in captured.out


def test_add(monkeypatch, capsys):
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    add_countries(countries)
    captured = capsys.readouterr()
    assert captured.out == "add_countries:\n ['Germany', 'France', 'Italy', 'Denmark', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine', 'Portugal']\n"


def test_remove(monkeypatch, capsys):
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    remove_countries(countries)
    captured = capsys.readouterr()
    assert captured.out == "remove_countries:\n ['Germany', 'Austria', 'Spain', 'Netherlands', 'Belgium']\n"



def test_find(monkeypatch, capsys):
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    find_countries(countries)
    captured = capsys.readouterr()
    assert captured.out == "find_country:\nNetherlands\n0\n"


def test_loop(monkeypatch, capsys):
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    loop_countries(countries)
    captured = capsys.readouterr()
    assert captured.out == (
        "loop_countries:\n"
        "Nr. 1: Germany\n"
        "Nr. 2: France\n"
        "Nr. 3: Italy\n"
        "Nr. 4: Austria\n"
        "Nr. 5: Spain\n"
        "Nr. 6: Netherlands\n"
        "Nr. 7: Belgium\n"
        "Nr. 8: Ukraine\n"
    )


def test_sort(monkeypatch, capsys):
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    sort_countries(countries)
    captured = capsys.readouterr()
    assert captured.out == (
        "sort_countries:\n"
        "Nr. 8: Ukraine\n"
        "Nr. 7: Spain\n"
        "Nr. 6: Netherlands\n"
        "Nr. 5: Italy\n"
        "Nr. 4: Germany\n"
        "Nr. 3: France\n"
        "Nr. 2: Belgium\n"
        "Nr. 1: Austria\n"
    )
