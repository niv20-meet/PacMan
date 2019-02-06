import turtle
import random

class Walls(object):
	movement=50
	def create_walls(turtle, maze_width,maze_height):
		turtle.pencolor('blue')
		turtle.pu()
		turtle.goto(-maze_width/2, -maze_height/2)
		turtle.pd()
		turtle.goto(-maze_width/2,maze_height/2)
		turtle.goto(maze_width/2,maze_height/2)
		turtle.goto(maze_width/2,-maze_height/2)
		turtle.goto(-maze_width/2, -maze_height/2)
		turtle.pu()
		turtle.goto(0,0)
		turtle.pd()
	def make_Wall(turtle, maze_width,maze_height):
		direction_list=["up","left","right","down"]
		index = random.randint(0,4)
		if direction_list[index]=="up":
						



