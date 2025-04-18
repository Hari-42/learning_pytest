def simplelist():
    animals = []
    animals.append('Tiger')
    animals.append('Lion')
    animals.append('Zebra')
    animals.append('Leopard')
    return animals

def givecarbrandnames():
    carbrands = []
    i = 0
    while i < 5:
        brand = input("carbrand > ")
        carbrands.append(brand)
        i += 1
    index = int(input("Name a number from 1-5 > "))
    print(carbrands[index - 1])

def add_countries(countries):
    countries.append('Portugal')
    countries.insert(3, 'Denmark')
    print('add_countries:\n', countries)


def remove_countries(countries):
    countries.pop()
    countries.pop(1)
    countries.remove('Italy')
    print('remove_countries:\n', countries)


def find_countries(countries):
    print('find_country:')
    print(countries[5])
    print(countries.index('Germany'))


def loop_countries(countries):
    print('loop_countries:')
    number = 1
    for country in countries:
        print(f'Nr. {number}: {country}')
        number += 1


def sort_countries(countries):
    print('sort_countries:')
    number = len(countries)
    for country in sorted(countries, reverse =True):
        print(f'Nr. {number}: {country}')
        number -= 1
