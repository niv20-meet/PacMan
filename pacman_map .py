import turtle
def PrintCor(x,y):
    print(x,y)



#turtle.bgpic("pacmanworld.gif")    
turtle.onscreenclick(PrintCor)

#while True :
	#print(turtle.pos())
turtle_pos= []

pacman = turtle.Turtle()
pacman.pu()
pacman.fd(1)

turtle_pos.append(turtle.pos())
#def move










turtle.speed(0)
turtle.ht()
turtle.pu()
turtle.goto(-215,230)
turtle.pd()
turtle.goto(-215,83)
turtle.goto(-139,83)
turtle.goto(-139,26)
turtle.goto(-221,26)
turtle.goto(-221,-17)
turtle.goto(-140,-17)
turtle.goto(-140,-70)
turtle.goto(-214,-70)
turtle.goto(-214,-251)
turtle.goto(219,-251)
turtle.goto(219,-73)
turtle.goto(142,-73)
turtle.goto(142,-15)

turtle.goto(225,-15)

turtle.goto(225,25)
turtle.goto(140,25)
turtle.goto(140,80)
turtle.goto(220,80)
turtle.goto(220,230)

turtle.goto(0,230)
turtle.goto(0,175)
turtle.goto(0,230)
turtle.goto(-215,230)

turtle.pu()
turtle.goto(-180,195)
turtle.pd()
turtle.goto(-140,195)
turtle.goto(-140,170)
turtle.goto(-180,170)
turtle.goto(-180,195)

turtle.pu()
turtle.goto(-100,195)
turtle.pd()
turtle.goto(-40,195)
turtle.goto(-40,170)
turtle.goto(-100,170)
turtle.goto(-100,195)

turtle.pu()
turtle.goto(45,195)
turtle.pd()
turtle.goto(100,195)
turtle.goto(100,170)
turtle.goto(45,170)
turtle.goto(45,195)


turtle.pu()
turtle.goto(140,195)
turtle.pd()
turtle.goto(180,195)
turtle.goto(180,170)
turtle.goto(140,170)
turtle.goto(140,195)


turtle.pu()
turtle.goto(-180,130)
turtle.pd()
turtle.goto(-130,130)
turtle.goto(-130,120)
turtle.goto(-180,120)
turtle.goto(-180,130)


turtle.pu()
turtle.goto(140,130)
turtle.pd()
turtle.goto(180,130)
turtle.goto(180,120)
turtle.goto(140,120)
turtle.goto(140,130)

turtle.ht()
turtle.pu()
turtle.goto(-100,-15)
turtle.pd()
turtle.goto(-85,-15)
turtle.goto(-85,-70)
turtle.goto(-100,-70)
turtle.goto(-100,-15)

turtle.pu()
turtle.goto(90,-20)
turtle.pd()
turtle.goto(105,-20)
turtle.goto(105,-75)
turtle.goto(90,-75)
turtle.goto(90,-20)

turtle.pu()
turtle.goto(-100,125)
turtle.pd()
turtle.goto(-88,125)
turtle.goto(-88,80)
turtle.goto(-44,80)
turtle.goto(-44,70)
turtle.goto(-88,70)
turtle.goto(-88,26)
turtle.goto(-100,26)
turtle.goto(-100,125)

turtle.pu()
turtle.goto(-50,130)
turtle.pd()
turtle.goto(54,130)
turtle.goto(54,117)
turtle.goto(10,117)
turtle.goto(10,71)
turtle.goto(-5,71)
turtle.goto(-5,117)
turtle.goto(-50,117)
turtle.goto(-50,130)

turtle.pu()
turtle.goto(90,130)
turtle.pd()
turtle.goto(100,130)
turtle.goto(100,25)
turtle.goto(90,25)
turtle.goto(90,70)
turtle.goto(45,70)
turtle.goto(45,80)
turtle.goto(90,80)
turtle.goto(90,130)


turtle.pu()
turtle.goto(90,130)
turtle.goto(105,130)
turtle.goto(105,25)
turtle.goto(90,25)
turtle.goto(90,70)
turtle.goto(45,70)
turtle.goto(45,80)
turtle.goto(90,80)
turtle.goto(90,130)

turtle.pu()
turtle.goto(55,35)
turtle.pd()
turtle.goto(55,-25)
turtle.goto(-55,-25)
turtle.goto(-55,35)
turtle.goto(55,35)

turtle.pu()
turtle.goto(-50,-60)
turtle.pd()
turtle.goto(50,-60)
turtle.goto(50,-75)
turtle.goto(10,-75)
turtle.goto(10,-120)
turtle.goto(-5,-120)
turtle.goto(-5,-75)
turtle.goto(-50,-75)
turtle.goto(-50,-60)

turtle.pu()
turtle.goto(100,-110)
turtle.pd()
turtle.goto(45,-110)
turtle.goto(45,-120)
turtle.goto(100,-120)
turtle.goto(100,-110)


turtle.pu()
turtle.goto(-100,-110)
turtle.pd()
turtle.goto(-45,-110)
turtle.goto(-45,-120)
turtle.goto(-100,-120)
turtle.goto(-100,-110)

turtle.pu()
turtle.goto(140,-110)
turtle.pd()
turtle.goto(180,-110)
turtle.goto(180,-120)
turtle.goto(150,-120)
turtle.goto(150,-165)
turtle.goto(140,-165)
turtle.goto(140,-110)

turtle.pu()
turtle.goto(-140,-110)
turtle.pd()
turtle.goto(-180,-110)
turtle.goto(-180,-120)
turtle.goto(-150,-120)
turtle.goto(-150,-165)
turtle.goto(-140,-165)
turtle.goto(-140,-110)

turtle.pu()
turtle.goto(-50,-160)
turtle.pd()
turtle.goto(50,-160)
turtle.goto(50,-170)
turtle.goto(10,-170)
turtle.goto(10,-215)
turtle.goto(-5,-215)
turtle.goto(-5,-170)
turtle.goto(-50,-170)
turtle.goto(-50,-160)

turtle.pu()
turtle.goto(50,-200)
turtle.pd()
turtle.goto(90,-200)
turtle.goto(90,-160)
turtle.goto(100,-160)
turtle.goto(100,-200)
turtle.goto(180,-200)
turtle.goto(180,-215)
turtle.goto(50,-215)
turtle.goto(50,-200)

turtle.pu()
turtle.goto(-50,-200)
turtle.pd()
turtle.goto(-90,-200)
turtle.goto(-90,-160)
turtle.goto(-100,-160)
turtle.goto(-100,-200)
turtle.goto(-180,-200)
turtle.goto(-180,-215)
turtle.goto(-50,-215)
turtle.goto(-50,-200)


turtle.pu()
turtle.goto(-214,-155)
turtle.pd()
turtle.goto(-185,-155)
turtle.goto(-185,-170)
turtle.goto(-214,-170)
turtle.goto(-214,-155)

turtle.pu()
turtle.goto(219,-155)
turtle.pd()
turtle.goto(185,-155)
turtle.goto(185,-170)
turtle.goto(219,-170)
turtle.goto(219,-155)


 
for i in (turtle_pos):
            print(i)
while True:
    pacman.fd(1)        

    def k1():
        pacman.setheading(90)
    def k2():
        pacman.setheading(180)
    def k3():
        pacman.setheading(270)
    def k4():
        pacman.setheading(0)

    turtle.onkeypress(k1, "Up")
    turtle.onkeypress(k2, "Left")
    turtle.onkeypress(k3, "Down")
    turtle.onkeypress(k4, "Right")

    turtle.listen() 

    for i in (turtle_pos):
            
    


turtle.mainloop()
            












          
         

















