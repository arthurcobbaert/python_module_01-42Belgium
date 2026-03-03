class Plant:
	def __init__(self, name, height):
		self.name = name
		self.height = height
	def get_info():
		return (f"- {self.name.capitalize()} Tree: {self.height}cm")

class FloweringPlant(Plant):
	def __init__(self, name, height, color):
		super().__init__(name, height)
		self.color = color
	def get_info(self):
		return (f"- {self.name.capitalize()}: {self.height}cm, {self.color} flowers (blooming)")

class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, color, prize):
		super().__init__(name, height, color)
		self.prize = prize
	def get_info(self):
		return (f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prizepoints: {self.prize}")

class GardenManager:
	total_gardens = 0

	class GardenStats():
	
