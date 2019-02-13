import turtle
import random

class Walls(object):
	def __init__(self):
		self.prevdirection = "up"
		self.size = 30
	def create_walls(self, maze_width,maze_height):
		self.borderT1=turtle.Turtle()
		self.borderT2=turtle.Turtle()
		self.movement=50
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
		for i in range(50):
			self.make_path(maze_width, maze_height)
	def swapturtles(self, direction):
		x1,y1 = self.borderT1.pos()
		x2,y2 = self.borderT2.pos()
		if direction == "up" :
			if x1==x2 and y2>y1:
				temp=self.borderT1
				self.borderT1=self.borderT2
				self.borderT2=temp

		if direction == "down":
			if x1==x2 and y2>y1:
				temp=self.borderT1
				self.borderT1=self.borderT2
				self.borderT2=temp 
		
		if direction == "left":
			if y1==y2 and x2<x1:
				temp=self.borderT1
				self.borderT1=self.borderT2
				self.borderT2=temp

		if direction == "right":
			if y1==y2 and x1<x2:
				temp=self.borderT1
				self.borderT1=self.borderT2
				self.borderT2=temp

	def make_path(self, maze_width,maze_height):
		#remeber to make shur prv diraction is not = to corrunt direction 
		x1,y1 = self.borderT1.pos()
		x2,y2 = self.borderT2.pos()
		direction_list=["up","left","right","down"]
		index = random.randint(0,3)
		self.swapturtles(direction_list[index])
		if direction_list[index]=="up":
			if x1==x2 :
				if self.prevdirection == "left":
					self.borderT2.goto(x2-self.size, y2)
					self.borderT2.goto(x2-self.size, y1+self.movement )
					self.borderT1.goto(x1,y1+self.movement)

				if self.prevdirection == "right":
					self.borderT2.goto(x2+self.size, y2)
					self.borderT2.goto(x2+self.size, y1+self.movement )
					self.borderT1.goto(x1,y1+self.movement)
			if y1==y2:
				self.borderT1.goto(x1,y1+self.movement)
				self.borderT2.goto(x2,y2+self.movement)

		if direction_list[index]=="down":
			if x1==x2 :
				if self.prevdirection == "left":
					self.borderT2.goto(x2-self.size, y2)
					self.borderT2.goto(x2-self.size, y1-self.movement )
					self.borderT1.goto(x1,y1-self.movement)

				if self.prevdirection == "right":
					self.borderT2.goto(x2+self.size, y2)
					self.borderT2.goto(x2+self.size, y1-self.movement )
					self.borderT1.goto(x1,y1-self.movement)
			if y1==y2:
				self.borderT1.goto(x1,y1-self.movement)
				self.borderT2.goto(x2,y2-self.movement)

		if direction_list[index]=="left":
			if x1==x2 :
				self.borderT1.goto(x1-self.movement,y1)
				self.borderT2.goto(x2-self.movement,y2)
			if y1==y2:
				if self.prevdirection == "up":
					self.borderT2.goto(x2, y2+self.size)
					self.borderT2.goto(x2-self.movement, y2+self.size )
					self.borderT1.goto(x1-self.movement,y1)

				if self.prevdirection == "down":
					self.borderT2.goto(x2, y2-self.size)
					self.borderT2.goto(x2-self.movement, y2-self.size )
					self.borderT1.goto(x1-self.movement,y1)
		if direction_list[index]=="right":
			if x1==x2 :
				self.borderT1.goto(x1+self.movement,y1)
				self.borderT2.goto(x2+self.movement,y2)
			if y1==y2:
				if self.prevdirection == "up":
					self.borderT2.goto(x2, y2+self.size)
					self.borderT2.goto(x2+self.movement, y2+self.size )
					self.borderT1.goto(x1+self.movement,y1)

				if self.prevdirection == "down":
					self.borderT2.goto(x2, y2-self.size)
					self.borderT2.goto(x2+self.movement, y2-self.size )
					self.borderT1.goto(x1+self.movement,y1)
		self.prevdirection = direction_list[index]
maze = Walls()
maze.create_walls(500,500)	

						
turtle.mainloop()


