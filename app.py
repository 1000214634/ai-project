import turtle
import random

# Set up the window
WIDTH = 800
HEIGHT = 600
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(WIDTH, HEIGHT)

# Set up the colors
PADDLE_COLOR = "white"
BALL_COLOR = "white"

# Set up the constants for the ball and paddles
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
PADDLE_SPEED = 20
BALL_SPEED = 5


# Set up the variables for the scores
player_a_score = 0
player_b_score = 0

# Set up the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color(BALL_COLOR)
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED * random.choice([-1, 1])
ball.dy = BALL_SPEED * random.choice([-1, 1])


# Set up the left paddle
paddle_left = turtle.Turtle()
paddle_left.shape("square")
paddle_left.color(PADDLE_COLOR)
paddle_left.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=PADDLE_WIDTH / 20)
paddle_left.penup()
paddle_left.goto(-(WIDTH / 2 - 50), 0)


# Set up the right paddle
paddle_right = turtle.Turtle()
paddle_right.shape("square")
paddle_right.color(PADDLE_COLOR)
paddle_right.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=PADDLE_WIDTH / 20)
paddle_right.penup()
paddle_right.goto(WIDTH / 2 - 50, 0)


# Set up the functions for moving the paddles
def paddle_left_up():
    y = paddle_left.ycor()
    y += PADDLE_SPEED
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= PADDLE_SPEED
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += PADDLE_SPEED
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= PADDLE_SPEED
    paddle_right.sety(y)


# Set up the keyboard bindings
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")


# Set up the pen for writing the scores
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, HEIGHT / 2 - 50)
pen.write(
    "Player A: {}  Player B: {}".format(player_a_score, player_b_score),
    align="center",
    font=("Courier", 24, "normal"),
)


# Define the collision detection function
def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    if distance < BALL_RADIUS + PADDLE_WIDTH / 2:
        return True
    else:
        return False


# Set up the game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce the ball off the top and bottom walls
    if (
        ball.ycor() > HEIGHT / 2 - BALL_RADIUS
        or ball.ycor() < -HEIGHT / 2 + BALL_RADIUS
    ):
        ball.dy *= -1

    # Bounce the ball off the left and right paddles
    if is_collision(ball, paddle_left) or is_collision(ball, paddle_right):
        ball.dx *= -1

    # If the ball goes off the left or right edge, reset it and add a point to the corresponding player
    if ball.xcor() > WIDTH / 2 - BALL_RADIUS:
        ball.goto(0, 0)
        ball.dx = -BALL_SPEED
        player_a_score += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(player_a_score, player_b_score),
            align="center",
            font=("Courier", 24, "normal"),
        ),

    elif ball.xcor() < -WIDTH / 2 + BALL_RADIUS:
        ball.goto(0, 0)
        ball.dx = BALL_SPEED
        player_b_score += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(player_a_score, player_b_score),
            align="center",
            font=("Courier", 24, "normal"),
        )
