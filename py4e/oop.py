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
        print(self.name, "Party count:", self.x)

# s = PartyAnimal("SAL")
# s.party()
# s.party()

# j = PartyAnimal("KIM")
# j.party()

class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
    
    def touchdown(self):
        self.points = self.points + 7
        print(self.name, "Points Now:", self.points)

s = PartyAnimal("Jill")
s.party()
s.party()

n = FootballFan("Noah")
n.touchdown()
n.party()
n.touchdown()
        
