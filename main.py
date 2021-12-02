import colorgram
from turtle import Turtle, Screen
from random import randint


def main():
    colors = colorgram.extract('image.jpg', 30) # create color list based on actual hirst dot painting
    rgb_list1 = []

    for i in range(0, len(colors)):
        next_color = colors[i]
        rgb = next_color.rgb
        rgb_list1.append(rgb)


    tim = Turtle()
    tim.speed("fastest")
    screen = Screen()
    screen.colormode(255)
    tim.penup()
    tim.hideturtle()
    starting_x = -200
    starting_y = 200
    tim.setx(starting_x)
    tim.sety(starting_y)

    row_count = 15
    dot_count = row_count ** 2 #square so as to keep shape of dots a square
    dot_counter = 0
    row_counter = 0
    dotsize = 15

    while dot_counter < dot_count:  # draw a Hirst dot painting, a square of multi colored dots
        if dot_counter % row_count == 0:
            row_counter += 1
            tim.setx(starting_x)
            tim.sety(starting_y - (row_counter * (dotsize * 2)))
        else:
            tim.dot(dotsize, rgb_list1[randint(0, len(rgb_list1) - 1)])
            tim.forward(dotsize * 2)
        dot_counter += 1

    screen.exitonclick()


main()
