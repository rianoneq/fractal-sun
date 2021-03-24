import turtle

t = turtle.Turtle()
t.speed(100)

def pentagon(x):
    for side in range(5):
        #print(side)
        t.color(colors[side%4])
        t.forward(x)
        t.left(72)
 
colors = ['black', 'violet', 'green', 'blue']
length = 10

for pent in range(100):
    pentagon(length)
    t.right(7)
    length+=3

if __name__ == "__main__":

    #close on click(don't closing automaticly)
    myWin = turtle.Screen()
    myWin.exitonclick()