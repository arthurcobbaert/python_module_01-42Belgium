class Plant:
	name: str
	height: int
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height
	def get_info() -> str:
		return (f"- {self.name.capitalize()} Tree: {self.height}cm")

class FloweringPlant(Plant):
	color: str
	def __init__(self, name: str, height: int, color: str):
		super().__init__(name, height)
		self.color = color
	def get_info(self) -> str:
		return (f"- {self.name.capitalize()}: {self.height}cm, {self.color} flowers (blooming)")

class PrizeFlower(FloweringPlant):
	prize: int
	def __init__(self, name: str, height: int, color: str, prize: int):
		super().__init__(name, height, color)
		self.prize = prize
	def get_info(self):
		return (f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prizepoints: {self.prize}")

class GardenManager:
	total_gardens = 0

	class GardenStats():
	
