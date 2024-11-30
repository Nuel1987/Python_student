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
