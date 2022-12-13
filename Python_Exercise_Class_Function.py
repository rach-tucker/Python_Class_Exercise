### Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement

# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal():
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def eat(self, int):
        self.energy = (self.energy + int)
        print(f"{self.name} is eating for {int} minutes. His energy level is now {self.energy}")

    def sleep(self, int):
        self.energy = (self.energy + int)
        print(f"{self.name} is sleeping for {int} minutes. His energy level is now {self.energy}")
    
    def play(self, int):
        self.energy = (self.energy - int)
        print(f"{self.name} is playing for {int} minutes. His energy level is now {self.energy}")


buddy = Animal('Buddy', 10)
buddy.eat(3)
buddy.sleep(100)

buddy.play(50)



