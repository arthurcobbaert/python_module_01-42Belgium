class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color
	def get_info(self):
		return (f"\n{self.name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self.color} color")
	def bloom(self):
		return (f"{self.name.capitalize()} is blooming beautifully!")

class Tree(Plant):
	def __init__(self, name, height, age, diameter):
		super(). __init__(name, height, age)
		self.diameter = diameter
	def get_info(self):
		return (f"\n{self.name.capitalize()} (Tree): {self.height}cm, {self.age} days, {self.diameter}cm diameter")
	def produce_shade(self):
		radius = self.height / 100
		shade = 3.14 * (radius ** 2)
		return (f"{self.name.capitalize()} provides {shade:.0f} square meters of shade")

class Vegetable(Plant):
	def __init__(self, name, height, age, harvest_season, nutritional_value):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	def get_info(self):
		return (f"\n{self.name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest \n{self.name.capitalize()} is rich in {self.nutritional_value}")

def ft_data():	
	print("=== Garden Plant Types ===")
	
	rose = Flower("rose", 25, 30, "red")
	print(rose.get_info())
	print(rose.bloom())
	
	oak = Tree("oak", 500, 1825, 50)
	print(oak.get_info())
	print(oak.produce_shade())
	
	tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
	print(tomato.get_info())
	
if __name__ == "__main__":
	ft_data()
