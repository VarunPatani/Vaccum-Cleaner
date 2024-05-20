import random
import turtle
import time


# Set up the screen
screen = turtle.Screen()
screen.setup(300, 300)

# Create a turtle object
vacuumCleaner = turtle.Turtle()
vacuumCleaner.shape("square")
vacuumCleaner.speed(0)

# Set the starting position of the turtle to the top-left corner
vacuumCleaner.penup()
vacuumCleaner.goto(-290, 290)  # Set the starting coordinates (-290, 290)
vacuumCleaner.pendown()


def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20  # Adjust this value depending on the size of your VC and spot


def move_and_turn():
    vacuumCleaner.setheading(270)  # Set VC's heading downward
    vacuumCleaner.forward(20)  # Move the VC down 20 pixels
    vacuumCleaner.setheading(180)  # Turn the VC to the left


# Function to move the VC horizontally to the right edge
def move_to_right_edge():
    vacuumCleaner.setheading(0)  # Set VC's heading to the right
    vacuumCleaner.forward(20)  # Move the VC to the right edge


# Function to move the VC horizontally to the left edge
def move_to_left_edge():
    vacuumCleaner.setheading(180)  # Set VC's heading to the left
    vacuumCleaner.forward(20)  # Move the VC to the left edge


# Create a list to store the spot turtles
spots = []


# Function to create an spot at a random position
def create_spot():
    spot = turtle.Turtle()
    spot.speed(0)
    spot.shape("circle")
    spot.color("red")
    spot.penup()
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    spot.goto(x, y)
    spots.append(spot)


# Function to check if the VC touches an spot, and as it touches remove spot
def check_collision():
    global spots
    for spot in spots:
        if is_collision(vacuumCleaner, spot):
            spot.hideturtle()
            spots.remove(spot)


def move():
    for i in range(29*1):
        move_to_right_edge()
        check_collision()
    move_and_turn()
    for i in range(29*1):
        move_to_left_edge()
        check_collision()
    move_and_turn()
    check_collision()


# Create 5 spots at random positions
for _ in range(15):
    create_spot()

# Move the VC until the screen is covered
while True:
    move()
    # Break the loop if the VC goes beyond the bottom edge
    if vacuumCleaner.ycor() < -290:
        break

# Final Prompts
time.sleep(0.5)
vacuumCleaner.clear()
vacuumCleaner.hideturtle()
vacuumCleaner.penup()
vacuumCleaner.goto(0, 0)
vacuumCleaner.write("Cleaning Completed, No Spots Remain",
                    align='center', font=('Times New Roman', 26, 'normal'))

# Keep the window open until it's manually closed
turtle.done()
