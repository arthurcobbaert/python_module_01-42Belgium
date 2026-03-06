class Plant:
	name: str
	height: int
	age: int
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age
class Flower(Plant):
	color: str
	def __init__(self, name: str, height: int, age: int, color: str):
		super().__init__(name, height, age)
		self.color = color
	def get_info(self) -> str:
		return (f"\n{self.name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self.color} color")
	def bloom(self) -> str:
		return (f"{self.name.capitalize()} is blooming beautifully!")

class Tree(Plant):
	diameter: int
	def __init__(self, name: str, height: int, age: int, diameter: int):
		super(). __init__(name, height, age)
		self.diameter = diameter
	def get_info(self) -> str:
		return (f"\n{self.name.capitalize()} (Tree): {self.height}cm, {self.age} days, {self.diameter}cm diameter")
	def produce_shade(self) -> str:
		radius: float = self.height / 100
		shade: float = 3.14 * (radius ** 2)
		return (f"{self.name.capitalize()} provides {shade:.0f} square meters of shade")

class Vegetable(Plant):
	harvest_season: str
	nutritional_value : str
	def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	def get_info(self) -> str:
		return (f"\n{self.name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest \n{self.name.capitalize()} is rich in {self.nutritional_value}")

def ft_data() -> None:
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
