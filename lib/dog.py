APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if isinstance(name_param, str) and 1 <= len(name_param) <= 25:
            self._name = name_param.title()
        else:
            raise ValueError(
                "Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, breed_param):
        if breed_param in APPROVED_BREEDS:
            self._breed = breed_param
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    
