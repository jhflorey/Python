from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()
        self.intelligence = 10
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()
        self.stealth = 10
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()
        self.strength = 10
        self.clever = 8
    def sacrifice(self):
        self.health -= 5
        return self
    def display_info(self):
        print("Samurai has:   %s in health, Romantic: %s, Clever: %s, Happiness: %s, Strength: %s" % (self.health, self.romantic, self.clever, self.happiness, self.strength))

samurai1 = Samurai()
print(samurai1.clever)
samurai1.sacrifice().sacrifice()
samurai1.sacrifice()
samurai1.display_info()