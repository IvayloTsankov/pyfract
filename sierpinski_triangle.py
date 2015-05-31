import turtle
t = turtle.Turtle()


def draw_sierpinski(t, length, depth, color_func):
    if depth==0:
        t.color(color_func())
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(t, length/2,depth-1, color_func)
        move(t, "forward", length/2)

        draw_sierpinski(t, length/2,depth-1, color_func)        
        move(t, "backward", length/2)

        t.left(60)
        move(t, "forward", length/2)

        t.right(60)
        draw_sierpinski(t, length/2,depth-1, color_func)

        t.left(60)
        move(t, "backward", length/2)

        t.right(60)


def move(t, direction, distance):
    t.up()

    if direction == "forward":
        t.forward(distance)
    elif direction == "backward":
        t.backward(distance)
    else:
        t.down()
        raise DirectionUnknownError

    t.down()


def get_color():
    distance_vector = int(t.distance(0, 0))

    red = distance_vector % 255
    green = 0
    blue = 0

    return (red, green, blue)


def main():
    # get screen instance
    window = turtle.Screen()

    factor = 900

    # prepare turtle drawing object
    turtle.colormode(255)
    t.speed(0)
    t.hideturtle()
    t.up()
    t.backward(factor/2)
    t.right(90)
    t.forward(factor/2)
    t.left(90)
    t.down()
    

    draw_sierpinski(t, factor, 5, get_color)

    window.exitonclick()    


if __name__ == "__main__":
    main()
