
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.owner = owner
        self.all_pets.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda pet: pet.name)
        return sorted_pets
