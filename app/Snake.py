class Snake:
	def __init__(self, start_data):
		self.height = start_data.height
		self.snake_id = "c6381a5a-fbdb-4695-bf10-b2beea256a4f"


		self.width = start_data.width
		self.snake = [s for s in start_data.snakes if s.id == self.snake_id]
		self.moves = ["north", "south", "east", "west"]
		self.move = moves[0]



def move(data):
	snake = [s for s in data.snakes if self.snake_id = s.id][0]
	pos = snake.coords
	head = pos[0]
	
	if nearWall(data):
		move = "west"

	return move



def nearWall(data):

	return true

