import turtle
import time
import random

score = 0
highscore = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("red")
comida.penup()
comida.goto(0, 100)

segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0		High Score: 0", align="center",font=("Courier", 12, "normal") )

def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def derecha():
	cabeza.direction = "right"
def izquierda():
	cabeza.direction = "left"


def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)
	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)
	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)
	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)


wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")
while True:
	wn.update()
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(0.5)
		cabeza.goto(0,0)
		cabeza.direction = "stop"
		for segmento in segmentos:
			segmento.goto(1000,1000)
		segmentos.clear()
		score = 0
		texto.clear()
		texto.write("Score: {}		High Score: {}".format(score, highscore), align="center",font=("Courier", 12, "normal") )


	if cabeza.distance(comida) < 19:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x, y)
		nuevosegmento = turtle.Turtle()
		nuevosegmento.speed(0)
		nuevosegmento.shape("square")
		nuevosegmento.color("grey")
		nuevosegmento.penup()
		segmentos.append(nuevosegmento)
		score += 1
		if score > highscore:
			highscore += 1
		texto.clear()
		texto.write("Score: {}		High Score: {}".format(score, highscore), align="center",font=("Courier", 12, "normal") )

	totalseg = len(segmentos)
	for index in range(totalseg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x, y)
	if totalseg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x, y)
	

	mov()
	time.sleep(0.1)
