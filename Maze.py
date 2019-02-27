import turtle
from turtle import *
import random

class Walls(object):
	def __init__(self):
		self.prevdirection = "up"
		self.size = 30
	def create_walls(self, maze_width,maze_height):
		self.borderT1=turtle.Turtle()
		self.borderT2=turtle.Turtle()
		self.borderT2.goto(0,-self.size)
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
		for i in range(500):
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
			if x1==x2 and y2<y1:
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

	def check_reverse(self,direction):
		if self.prevdirection == "left":
			return not direction == "right"
		if self.prevdirection == "right":
			return not direction == "left"
		if self.prevdirection == "up":
			return not direction == "down"
		if self.prevdirection == "down":
			return not direction == "up"

	def make_path(self, maze_width,maze_height):
		#remeber to make shur prv diraction is not = to corrunt direction 
		x1,y1 = self.borderT1.pos()
		x2,y2 = self.borderT2.pos()
		print(x1,y1)
		print(x2,y2)
		direction_list=["up","left","right","down"]
		index = random.randint(0,3)
		while(not self.check_reverse(direction_list[index]) or self.IsHitBorder(direction_list[index], maze_width, maze_height)):
			index = random.randint(0,3)
		self.swapturtles(direction_list[index])
		print(index)
		if direction_list[index]=="up":
			if x1==x2:
				if self.prevdirection == "left":
					print("ul")
					self.borderT2.goto(x2-self.size, y2)
					self.borderT1.goto(x1,y1+self.movement)
					self.borderT2.goto(x2-self.size, y1+self.movement )    


				if self.prevdirection == "right":
					print("ur")
					self.borderT2.goto(x2+self.size, y2)
					self.borderT1.goto(x1,y1+self.movement)
					self.borderT2.goto(x2+self.size, y1+self.movement )
			if y1==y2:
				print("u")
				self.borderT1.goto(x1,y1+self.movement)
				self.borderT2.goto(x2,y2+self.movement)

		if direction_list[index]=="down":
			if x1==x2 :
				
				if self.prevdirection == "left":
					print("d")
					self.borderT2.goto(x2-self.size, y2)
					self.borderT1.goto(x1,y1-self.movement)
					self.borderT2.goto(x2-self.size, y1-self.movement )

				if self.prevdirection == "right":
					print("d")
					self.borderT2.goto(x2+self.size, y2)
					self.borderT1.goto(x1,y1-self.movement)
					self.borderT2.goto(x2+self.size, y1-self.movement )
			if y1==y2:
				print("d")
				self.borderT1.goto(x1,y1-self.movement)
				self.borderT2.goto(x2,y2-self.movement)

		if direction_list[index]=="left":
			if x1==x2 :
				print("l")
				self.borderT1.goto(x1-self.movement,y1)
				self.borderT2.goto(x2-self.movement,y2)
			if y1==y2:
				
				if self.prevdirection == "up":
					print("l")
					self.borderT2.goto(x2, y2+self.size)
					self.borderT1.goto(x2-self.movement,y1)
					self.borderT2.goto(x2-self.movement, y2+self.size )

				if self.prevdirection == "down":
					print("l")
					self.borderT2.goto(x2, y2-self.size)
					self.borderT1.goto(x2-self.movement,y1)
					self.borderT2.goto(x2-self.movement, y2-self.size )
		if direction_list[index]=="right":
			if x1==x2 :
				print("r")
				self.borderT1.goto(x1+self.movement,y1)
				self.borderT2.goto(x2+self.movement,y2)
			if y1==y2:

				if self.prevdirection == "up":
					print("r")
					self.borderT2.goto(x2, y2+self.size)
					self.borderT1.goto(x2+self.movement,y1)
					self.borderT2.goto(x2+self.movement, y2+self.size )

				if self.prevdirection == "down":
					print("r")
					self.borderT2.goto(x2, y2-self.size)
					self.borderT1.goto(x2+self.movement,y1)
					self.borderT2.goto(x2+self.movement, y2-self.size )
		self.prevdirection = direction_list[index]
		print("reached")
	def IsHitBorder(self, direction, maze_width, maze_height):
		final_x = 0
		final_y = 0
		if direction == "up" :
			final_y = self.borderT2.ycor() + self.movement
		if direction == "down" :
			final_y = self.borderT2.ycor() - self.movement
		if direction == "right" :
			final_x = self.borderT2.xcor() + self.movement
		if direction == "left" :
			final_x = self.borderT2.xcor() - self.movement
		return not(final_y < maze_height/2 and final_y > -maze_height/2 and final_x < maze_width/2 and final_x > -maze_width/2)


maze = Walls()
maze.create_walls(500,500)	

						
turtle.mainloop()


