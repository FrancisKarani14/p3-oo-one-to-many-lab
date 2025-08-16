class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner= None):
        if pet_type  not in Pet.PET_TYPES:
            raise ValueError (f"invalid value {pet_type} should be one of{Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")


class Owner:
    # all = []
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self
