import winsound
import turtle
import random
import os


turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
maze_maker = turtle.Turtle()
counter =  turtle.Turtle()
maze_maker.pensize(3)
wall_length = 25
width = 10
maze_maker.showturtle()
start_pos=(50, -50)
tess.penup()
tess.goto(start_pos)
maze_maker.speed(0)

# Build the maze

for i in range (50):
   width+=10
   wall_distance=random.randint(10,width-5)
   maze_maker.forward(wall_distance)
   maze_maker.forward(20)
   maze_maker.left(90)
   maze_maker.forward(20)
   maze_maker.back(20)
   maze_maker.right(90)
   maze_maker.penup()
   maze_maker.forward(wall_length)
   maze_maker.pendown()
   maze_maker.forward(wall_length-wall_distance+width)
   maze_maker.forward(20)
   maze_maker.right(90)
for i in range(4):
   width+=10
   wall_distance=random.randint(10,width-5)
   maze_maker.forward(wall_distance+wall_length)
   maze_maker.forward(wall_length-wall_distance+width)
   maze_maker.forward(20)
   maze_maker.right(90)

# The next four functions are our "event handlers".
def h1():
   tess.forward(10)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()  # Close down the turtle window

# --- END: Replacement block ---

# timer
font_setup = ("Arial", 20, "normal")
timer = 0
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

#-----countdown writer-----
counter.hideturtle()
counter.penup()
counter.goto(300,300)

#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer >= 100:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    wn.onkey(None, "Up")
    wn.onkey(None, "Left")
    wn.onkey(None, "Right")
    return
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer += 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# Play background music
if os.path.exists("flow.wav"):
    # Combine flags with the | (pipe) character
    # SND_FILENAME: Tells it the 'flow.wav' is a path
    # SND_ASYNC:    Plays in the background (so your game doesn't freeze)
    # SND_LOOP:     Makes the music repeat
    flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    winsound.PlaySound("flow.wav", flags)
else:
    print(f"Warning: Music file not found at {"flow.wav"}")
    
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()