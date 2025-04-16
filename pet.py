class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.tricks = []  # List to store tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Hunger decreased, happiness increased!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy increased!")
    
    def play(self):
        if self.energy >= 2:
            self.happiness = min(10, self.happiness + 2)
            self.energy = max(0, self.energy - 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing. Happiness increased, energy decreased!")
        else:
            print(f"{self.name} is too tired to play.")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks known: {len(self.tricks)}") 
        else:
            print("No tricks known.")

     # Bonus methods
    def train(self, trick):
        if self.energy >= 3:  # Training requires energy
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train right now.")
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
  


