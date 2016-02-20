class Snake:
	def __init__(self, start_data):
		self.height = start_data.height
		self.snake_id = "c6381a5a-fbdb-4695-bf10-b2beea256a4f"


		self.width = start_data.width
		self.snake = [s for s in start_data.snakes if s.id == self.snake_id]
		self.moves = ["north", "south", "east", "west"]
		self.move = moves[0]





def nearWall(data):
	print data

def update(data):
	