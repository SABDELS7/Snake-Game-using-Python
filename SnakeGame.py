# import packages
import turtle
import random
import time

# CREATING USER INTERFACE
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#000000")
 
# CREATING BORDER
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-250, 250)  
turtle.pendown()
turtle.color("red")
for _ in range(4):
    turtle.forward(500)
    turtle.right(90)
turtle.penup()
turtle.hideturtle()
 
# SCORE
score=0
delay=0.1
 
# SNAKE
snake=turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction ='stop'
 
# FOOD
fruit= turtle.Turtle()
fruit.speed()
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)
 
old_fruit= []
 
# SCORING
scoring= turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ",align="center",font=("Courier",24,"bold"))

# DEFINE HOW TO MOVE
def snake_go_up():
    if snake.direction != "Down":
        snake.direction = "Up"
        
def snake_go_down():
    if snake.direction != "Up":
        snake.direction = "Down"
        
def snake_go_right():
    if snake.direction != "Left":
        snake.direction = "Right"
        
def snake_go_left():
    if snake.direction != "Right":
        snake.direction = "Left"
        
def move():
    if snake.direction == "Up":
        y=snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "Down":
        y=snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "Right":
        x=snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "Left":
        x=snake.xcor()
        snake.setx(x - 20)
                    
# KEYBOARD BINDING
screen.listen()        
screen.onkeypress(snake_go_up,"Up")       
screen.onkeypress(snake_go_down,"Down")       
screen.onkeypress(snake_go_right,"Right")       
screen.onkeypress(snake_go_left,"Left")

# MAIN LOOP 
while True:
    screen.update() 
    
    # SNAKE & FRUIT CLISION
    if snake.distance(fruit) < 20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        fruit.goto(x , y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24 , "bold"))
        delay -= 0.001
        
        # CREATING NEW FOOD
        new_fruit= turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)
        
    # ADDING BALL TO SNAKE
    for i in range(len(old_fruit)-1, 0, -1):
        a = old_fruit[i-1].xcor()
        b = old_fruit[i-1].ycor()
        
        old_fruit[i].goto(a , b)
        
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        
        old_fruit[0].goto(a , b)
        
    move()
        
    # SNAKE & BORDER COLISION
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0 , 0)
        scoring.write("      Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30 , "bold"))
    
    # SNAKE COLISIONS
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0 , 0)
            scoring.write("      Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30 , "bold"))
            break
    
    time.sleep(delay)

turtle.done()                