import turtle

def draw_moon(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def main():
    turtle.speed(2)  # Set the drawing speed

    # Draw the moon
    draw_moon(100, "white")  # You can adjust the radius and color as needed

    # Hide the turtle
    turtle.hideturtle()

    # Keep the window open
    turtle.mainloop()

if __name__ == "__main__":
    main()
