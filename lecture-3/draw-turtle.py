import turtle

window = turtle.Screen()
window.bgcolor("blue") 
    
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(1000)

def square_steps():
    
    brad.forward(100)
 
    for i in range(1,4):
        
        brad.right(90)
        brad.forward(100)
    
    brad.right(90)

def draw_square():

    square_steps()

def draw_cir_w_square():
    
    iter = 0

    draw_square()

    while iter<361:

        brad.right(8)

        draw_square()

        iter = iter + 8 

draw_cir_w_square()

angie = turtle.Turtle()
angie.shape("turtle")
angie.color("red")
angie.speed(100)

def draw_pure_circle():
    angie.left(90)
    angie.forward(100)
    angie.left(90)
    angie.circle(100) 

    angie.right(90)
    angie.forward(45)
    angie.left(90)
    angie.circle(145)
    
draw_pure_circle()

pedro = turtle.Turtle()
pedro.shape("arrow")
pedro.color("black")
pedro.speed(5)

def draw_triangle():
    pedro.right(30)
    pedro.forward(400)
    pedro.right(150)
    pedro.forward(692)

    pedro.right(120)
    pedro.forward(692)
    
    pedro.right(120)
    pedro.forward(692)

draw_triangle()

jose = turtle.Turtle()
jose.shape("arrow")
jose.color("white")
jose.speed(5)

def draw_circle_triangle():

    jose.left(90)
    jose.forward(400)
    jose.left(90)
    jose.circle(400)

draw_circle_triangle()

window.exitonclick()
