def simplelist():
    # TODO: Create an empty list called animals
    # TODO: Add an animal called Tiger
    # TODO: Add an another animal called Lion
    # TODO: Add an another animal called Zebra
    # TODO: Add an another animal called Leopard
    # TODO: Return the list
    pass


def givecarbrandnames():
    # TODO: Create an empty list called carbrands
    # TODO: Allow the user, to only give 5 carbrands
    # TODO: let the user choose from 1 to 5
    # Todo: print the preferred indexed carbrand
    pass


def countrieslist():
    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    add_countries(countries)

    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    remove_countries(countries)

    countries = ['Germany', 'France', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium', 'Ukraine']
    find_countries(countries)
    loop_countries(countries)
    sort_countries(countries)

def add_countries(countries):
    # TODO: add Portugal at the end of the list
    # TODO: add Denmark at Index 3
    print('add_countries:\n', countries)


def remove_countries(countries):
    # TODO: remove the last country from the list
    # TODO: remove the country at Index 1
    # TODO: remove Italy from the list
    print('remove_countries:\n', countries)


def find_countries(countries):
    print('find_country:')
    # TODO: print the country at Index 5
    # TODO: print the position of Germany
    pass


def loop_countries(countries):
    print('loop_countries:')
    # TODO: print all countries in the list. output must be 'Nr. x: countryname', for example 'Nr. 1: Germany'


def sort_countries(countries):
    print('sort_countries:')
    # TODO: print all countries ordered by Name (descending). output must be 'Nr. x: countryname', for example 'Nr. 8: Ukraine'
