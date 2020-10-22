import turtle

axiom = "FX"
rules = {"X": "X+YF+", "Y": "-FX-Y"}
iterations = 8  # TOP: 16
angle = 90
colors = ["blue", "green", "pink", "navy", "purple", "skyblue", "gray"]

#make a string commanding what doing for fractal drawing
def make_my_system(axiom, iters, rules, t):
    opening = axiom
    if iters == 0:
        return opening
    else:
        for I in range(iters):
            genius_formula_container = []
            for i in opening:
                if i in rules:
                    genius_formula_container.append(rules[i])
                else:
                    genius_formula_container.append(i)

            ending = "".join(genius_formula_container)

            opening = ending
            full_string = opening

        return full_string

#reading command string and drawing a fractal via this string
def draw_my_fractal(t, algorithm, angle, distance):
    for act in algorithm:
        if act == "F":
            t.forward(distance)
        elif act == "-":
            t.left(angle)
        elif act == "+":
            t.right(angle)
    

def settings(t, window,iterations=iterations):
    #t.color('red')
    window.bgcolor('black')
    t.speed(0)
    t.hideturtle()
    t.up()
    t.backward(2*(iterations))
    t.left(angle)
    t.down()


def zero_fractal_position(t):
    pos = 0.00, 0.00
    t.up()
    t.setpos(pos)
    t.down()


def main(iterations=iterations, axiom=axiom, rules=rules, angle=angle, distance=12):
    t = turtle.Turtle()
    window = turtle.Screen()
    algorithm = make_my_system(axiom, iterations, rules, t)
    
    for n in colors:
        t.color(n)
        settings(t, window)
        zero_fractal_position(t)

        draw_my_fractal(t, algorithm, angle, distance)

    window.exitonclick()


if __name__ == "__main__":
    main()
