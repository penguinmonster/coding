import turtle

# Create a turtle object
t = turtle.Turtle()

# Initial side length of the square
side_length = 50

# Number of squares to draw
num_squares = 5

# Loop to draw squares of increasing sizes
for _ in range(num_squares):
    # Draw a square
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    
    # Increase the side length for the next square
    side_length += 50

# Close the turtle graphics window
turtle.done()
