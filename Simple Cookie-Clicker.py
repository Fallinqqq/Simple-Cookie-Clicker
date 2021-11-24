import turtle
# registers window/application 
app = turtle.Screen()
app.title("Cookie Clicker by Grace")
app.bgcolor("light blue")

app.register_shape("cookie.gif")

# The cookie shape and function within the window/application
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

# adding the function to click on the cookie and how many clicks were clicked
clicks = 0

total_clicks = turtle.Turtle()
total_clicks.hideturtle()
total_clicks.color("white")
total_clicks.penup()
total_clicks.goto(0, 200)
total_clicks.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    total_clicks.clear()
    total_clicks.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    
cookie.onclick(clicked)
app.mainloop()