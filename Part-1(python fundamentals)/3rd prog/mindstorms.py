import turtle

def draw_sqr(brad):
    i=0
    while i<4:
        brad.forward(100)
        brad.right(90)
        i+=1

def draw_shapes():
    window=turtle.Screen()
    window.bgcolor("green")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(8)
    
    k=0
    while(k<36):
        draw_sqr(brad)
        brad.right(10)
        k+=1
    #scar=turtle.Turtle()
    #scar.shape("arrow")
    #scar.color("blue")
    #scar.circle(70)
    #bar=turtle.Turtle()
    #bar.shape("turtle")
    #bar.color("black")
    #j=0
    #while(j<3):
    #    brad.forward(200)
    #    brad.right(120)
    #    j+=1
    
    window.exitonclick()
draw_shapes()
