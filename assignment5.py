#defining a class
class Smartphone:
    def __init__(self, type, model, dimension, sim):
        self.type = type
        self.model = model
        self.dimension = dimension
        self.sim = sim
    
    def turn_on(self):
        return f"The {self.type} {self.model} with {self.sim} and {self.dimension} is turned on."
    
    def turn_off(self):
        return f"The {self.type} {self.model} with {self.sim} and {self.dimension} is turned off."
    
    #bring class to live
if __name__ == "__main__":
    smartphone1 = Smartphone("iphone", "15", "2 sims", "115 x 61 x 11.6 mm" )
    smartphone2 = Smartphone("iphone", "15", "2 sims", "115 x 61 x 11.6 mm" )

#interatcing with objects
print(smartphone1.turn_on())
print(smartphone2.turn_off())

print(
    "\n")
# Another class defined
class Superhero:
    def __init__(self, name, powers, secret_identity, origin):
        self.name = name
        self.powers = powers
        self.secret_identity = secret_identity
        self.origin = origin

    def use_power(self):
        return f"{self.name} is using their power: {self.powers}"

    def reveal_identity(self):
        return f"Secret Identity: {self.secret_identity}"

    def introduce(self):
        return f"Hello! I am {self.name} from {self.origin}. My superpower is {self.powers}."

# Subclass for Flying Heroes
class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, origin, altitude):
        super().__init__(name, "Flight", secret_identity, origin)
        self.altitude = altitude

    # Overriding the use_power method for specific behavior
    def use_power(self):
        return f"{self.name} is flying at {self.altitude} meters above the ground!"

    def fly(self):
        return f"{self.name} is soaring through the skies!"

# Subclass for Strength Heroes
class StrengthHero(Superhero):
    def __init__(self, name, secret_identity, origin, strength_level):
        super().__init__(name, "Super Strength", secret_identity, origin)
        self.strength_level = strength_level

    # Overriding the use_power method for specific behavior
    def use_power(self):
        return f"{self.name} is lifting a {self.strength_level}-ton object with ease!"

    def super_strength(self):
        return f"{self.name} is showing off their superhuman strength!"

# Instantiate objects of each superhero class
superhero1 = FlyingHero("SkyBoss", "Kobby Nuel", "Earth", 5000)
superhero2 = StrengthHero("Iron Titan", "Kwaku Tih", "Mars", 50)

# Interacting with the objects and demonstrating polymorphism
print(superhero1.introduce())
print(superhero1.use_power())  # Polymorphism: FlyingHero overrides use_power
print(superhero1.fly())

print("\n")

print(superhero2.introduce())
print(superhero2.use_power())  # Polymorphism: StrengthHero overrides use_power
print(superhero2.super_strength())
