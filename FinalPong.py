import turtle
import time


counter = 2
FPS = 1/60
score1 = 0
score2 = 0
prev_score1 = 0
prev_score2 = 0





# screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("brown")
screen.setup(width=800, height=600)
screen.tracer(0)





# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
# ball.speed(0)
dx = 2
dy = 2





# score mechanism
writer = turtle.Turtle()
writer.penup()
writer.goto(0,250)
writer.write(f"{score1} | {score2}", font=("OpenSans",21,"bold"), align="center")
writer.hideturtle()

pen = turtle.Turtle()
pen.penup()
pen.goto(-120,250)
pen.write(f"Prev: {prev_score1}", font=("OpenSans",20,"bold"), align="right")
pen.hideturtle()


pen2 = turtle.Turtle()
pen2.penup()
pen2.goto(120,250)
pen2.write(f"Prev: {prev_score2}", font=("OpenSans",20,"bold"), align="left")
pen2.hideturtle()




# paddle creation
pad = turtle.Turtle()
pad.color("orange")
pad.shape("square")
pad.shapesize(stretch_len= .50, stretch_wid=3) # this method changes the shape op an turtle object.
pad.penup()
pad.goto(-380,0)
pad.dy = 30

pad2 = turtle.Turtle()
pad2.color("orange")
pad2.shape("square")
pad2.shapesize(stretch_len= .50, stretch_wid=3)
pad2.penup()
pad2.goto(380,0)
pad2.dy = 30









def pad_up():
	if pad.ycor() + 20.50 < 280:
	    pad.sety(pad.ycor() + pad.dy)

def pad_down():
	if pad.ycor() - 20.50 > -280:
		pad.sety(pad.ycor() - pad.dy)

def pad2_up():
	if pad2.ycor() + 20.50 < 280:
	    pad2.sety(pad2.ycor() + pad2.dy)

def pad2_down():
	if pad2.ycor() - 20.50 > -280:
		pad2.sety(pad2.ycor() - pad2.dy)

screen.listen()
screen.onkeypress(pad_up, "w")
screen.onkeypress(pad_down, "s")

screen.onkeypress(pad2_up, "Up")
screen.onkeypress(pad2_down, "Down")












while True:
	
	ball.setx(ball.xcor() + dx)
	ball.sety(ball.ycor() + dy)

	# tom and down
	if ball.ycor() > 240:
		dy *= -1 
	elif ball.ycor() < -290:
		dy *= -1




	# left and right

	if ball.xcor() > 390:
		dx *= -1
		ball.goto(0,0)
	elif ball.xcor() < -390:
		dx *= -1
		ball.goto(0,0)


		




		# paddle 1 movement
	if ball.xcor() < -360 and ball.ycor() < pad.ycor() + 50 and ball.ycor() > pad.ycor() - 50:
		dx *= -1
		dx += 2
		score1 += 1
		writer.clear()
		writer.write(f"{score1} | {score2}", font=("OpenSans",21,"bold"), align="center")

		# paddle 1 movement
	if ball.xcor() > 360 and ball.ycor() < pad2.ycor() + 50 and ball.ycor() > pad2.ycor() - 50:
		dx *= -1
		score2 += 1
		writer.clear()
		writer.write(f"{score1} | {score2}", font=("OpenSans",21,"bold"), align="center")		
	

	# reset mechanism

	if ball.xcor() == 0 and ball.ycor() == 0:
		prev_score1 = score1
		prev_score2 = score2
		pen.clear()
		pen.write(f"Prev: {prev_score1}", font=("OpenSans",20,"bold"), align="right")
		pen2.clear()
		pen2.write(f"Prev: {prev_score2}", font=("OpenSans",20,"bold"), align="left")
		score2 = 0
		score1 = 0
		dx = 2
		writer.clear()
		writer.write(f"{score1} | {score2}", font=("OpenSans",21,"bold"), align="center")

	
	
	screen.update()
	time.sleep(FPS)
