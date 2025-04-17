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