from turtle import *
import turtle
turtle.ht()
direction = "Up"
class player(Turtle):
	def __init__(self,x,y,speed,color):
		Turtle.__init__(self)
		self.goto(x,y)
		self.x=x
		self.y=y
		self.color(color)
		self.speed(speed)
		self.speed = speed
		turtle.register_shape("pacm.gif") 
		self.shape("pacm.gif")
		self.penup()
	def movePacMan (self):
		global direction
		if direction == "Right" :
			self.x = self.x + self.speed
		if direction == "Left" :
			self.x = self.x - self.speed
		if direction == "Up" :
			self.y = self.y + self.speed
		if direction=="Down" :
			self.y = self.y - self.speed
		self.goto(self.x,self.y)










turtle.listen()
def up():
    global direction #snake direction is global (same everywhere)
    direction= "Up"
    
    #Change direction to up
 #Update the snake drawing <- remember me later
    print("You pressed the up key!")
turtle.onkeypress(up, "Up") # Create listener for up key


turtle.listen()
def down():
    global direction #snake direction is global (same everywhere)
    direction= "Down" #Change direction to up #Update the snake drawing <- remember me later
    print("You pressed the down key!")
turtle.onkeypress(down, "Down")
turtle.listen()



def left():
    global direction #snake direction is global (same everywhere)
    direction="Left" #Change direction to up
#Update the snake drawing <- remember me later
    print("You pressed the left key!")
turtle.onkeypress(left, "Left")
turtle.listen()




def right():
    global direction #pacman direction is global (same everywhere)
    direction= "Right" #Change direction to up
 #Update pacman drawing <- remember me later
    print("You pressed the right key!")
turtle.onkeypress(right, "Right")
turtle.listen()



test = player(0,0,3,"red")

while True:
	test.movePacMan()

turtle.mainloop()