# Function to draw a square of a given size.
def draw_square(size):
    # Print each row of the square.
    for i in range(size):
        print("* " * size)


# Call the function with a size of 7.
draw_square(7)