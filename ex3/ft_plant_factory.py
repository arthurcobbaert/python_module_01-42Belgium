class Plant:
	name: str
	height: int
	age: int
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age
	def get_info(self) -> str:
		return (f"Created: {self.name} ({self.height}cm, {self.age} days)")

def ft_data() -> None:
	plants: list[Plant] = [
		Plant("Rose", 25, 30),
		Plant("Oak", 200, 365),
		Plant("Cactus", 5, 90),
		Plant("Sunflower", 80, 45),
		Plant("Fern", 15, 120),
	]
	count: int = 0
	print("=== Plant Factory Output ===")
	for plant in plants:
		print(plant.get_info())
		count += 1
	print(f"\nTotal plants created: {count}")

if __name__ == "__main__":
	ft_data()
