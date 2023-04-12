from Object_oriented_programming import PartyAnimal

print('-' * 120)


class CricketFan(PartyAnimal):
    poits = 0

    def six(self):
        self.poits = self.poits + 6
        self.party()
        print(self.name, 'points', self.poits)


s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))
