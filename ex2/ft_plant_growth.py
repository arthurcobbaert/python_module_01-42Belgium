class Plant:
	def __init__(self, name, height, old):
		self.name = name
		self.height = height
		self.old = old

	def grow(self):
		self.height += 1

	def age(self):
		self.old += 1

	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.old} days old"

def ft_data():
	rose = Plant("Rose", 25, 30)
	print("=== Day 1 ===")
	print(rose.get_info())

	for i in range(1, 7):
		rose.grow()
		rose.age()
	print("=== Day 7 ===")
	print(rose.get_info())
	print(f"Growth this week: +6cm")

if __name__ == "__main__":
	ft_data()
