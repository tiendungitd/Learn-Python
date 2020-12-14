from turtle import Turtle, Screen, colormode
import random
tim = Turtle()
tim.shape("turtle")
tim.color("black")
tim.hideturtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(num_sides):
    angle = 360 /num_sides
    for _ in range(num_sides):
      tim.forward(100)
      tim.right(angle)
def draw_shape_side():
    for shape_side_n in range(3,11):
        draw_shape(shape_side_n)
        tim.color(random_color())
        #tim.color(random.choice(colors))

def random_step():
    direction = [0, 90, 180, 270]
    for _ in range(200):
        tim.color(random.choice(colors))
        tim.pensize(10)
        tim.speed(0)
        tim.forward(30)
        tim.setheading(random.choice(direction))

def spirograph(size_of_gap):
    turn = int(360/size_of_gap)
    for _ in range(turn):
        tim.speed(0)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


spirograph(10)
screen = Screen()
screen.exitonclick()
