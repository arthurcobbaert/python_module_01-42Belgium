class Plant:
	name: str
	height: int
	old: int
	def __init__(self, name: str, height: int, old: int) -> None:
		self.name = name
		self.height = height
		self.old = old


def ft_data():
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)
	print("=== Garden Plant Registry ===")
	print(f"{rose.name}: {rose.height}cm, {rose.old} days old")
	print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.old} days old")
	print(f"{cactus.name}: {cactus.height}cm, {cactus.old} days old")

if __name__ == "__main__":
	ft_data()
