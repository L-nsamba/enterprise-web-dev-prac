# class PartyAnimal:
#     def __init__(self):
#         self.x = 0

#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)

# an = PartyAnimal()

# an.party()
# an.party()
# an.party()

class PartyAnimal:
    def __init__(self, name):
        self.x = 0
        self.name = name

    def party(self):
        self.x = self.x + 1
        print(self.name, "party_count", self.x)

s = PartyAnimal("SAL")
s.party()
s.party()

j = PartyAnimal("KIM")
j.party()
