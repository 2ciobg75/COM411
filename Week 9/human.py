class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = self.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        new_energy = self.energy + amount
        if new_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
        else:
            self.energy = new_energy

    def move(self, distance):
        new_energy = self.energy - distance
        if new_energy < 0:
            self.energy = 0
        else:
            self.energy = new_energy


if __name__ == "__main__":

    human = Human()
    human.display()
