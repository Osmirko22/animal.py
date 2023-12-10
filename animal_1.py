class Animal:
    def __init__(self, chip=None):
        self.chip = chip

    def __repr__(self):
        return f'{self.__class__.__name__}(chip={self.chip!r})'


class Human(Animal):
    pass


class Person(Human):
    def __init__(self, name, tax_number):
        super().__init__()
        self.name = name
        self.tax_number = tax_number

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, tax_number={self.tax_number!r})'


class Vaccine:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, manufacturer={self.manufacturer!r})'


class Chip:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(number={self.number!r})'


class AnimalIDChip(Chip):
    pass


class Pet(Animal):
    def __init__(self, owner, name, chip=None):
        super().__init__(chip)
        self.name = name
        self.owner = owner  

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(name={self.name!r}, owner={self.owner!r}, chip={self.chip!r})'


if __name__ == '__main__':
    # Example usage
    person = Person(name='John Doe', tax_number='123-456-789')
    vaccine = Vaccine(name='COVID-19', manufacturer='Pfizer')
    animal_chip = AnimalIDChip(number='A123456')

    pet_dog = Pet(owner=person, name='Buddy', chip=animal_chip)
    print(pet_dog)

    pet_cat = Pet(owner=person, name='Whiskers')
    print(pet_cat)
