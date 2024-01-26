import turtle
import random
from tkinter import *


#tkinter variables start here
root = Tk()#this is the tkinter "window", the base where everything happens
root.geometry("750x225")
root.configure(bg="grey23")
root.title("Snake Menu")

#diffentry and gmentry change based on the user input on tkinter's buttons
diffentry = " "
gmentry = " "

#these var1-3 are important in making sure each button appears one after another
var = StringVar()
var2 = StringVar()
var3 = StringVar()
#tkinter varlables end here
#tkinter will run a menu that will use input to determine turtle variables

#turtle variables start here
width = 500 #window resolution
height = 500
food_size = 10
score = 1
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
#turtle variables end here

welcome_label=Label(root, text="Welcome to Snake! Please select a gamemode and difficulty.", bg="grey23", fg="white")
welcome_label.config(font=("Arial", 18))
welcome_label.pack()


def gamemode_selected():
    global var
    gamemode_label = Label(root, text="Gamemode: " + gmentry, bg="grey23", fg="white")
    gamemode_label.pack()
    classic_button.pack_forget()
    ramping_button.pack_forget()
    var.set("next")

def gamemode_selected_classic():
    global gmentry
    gmentry = "CLASSIC"
    gamemode_selected()

def gamemode_selected_ramping():
    global gmentry
    gmentry = "RAMPING DIFFICULTY"
    gamemode_selected()

classic_button = Button(root, text="Classic", command=gamemode_selected_classic, bg="grey8", fg="white")
classic_button.config(font=("Arial", 14))
classic_button.pack()

ramping_button = Button(root, text="Ramping Difficulty", command=gamemode_selected_ramping, bg="grey8", fg="red")
ramping_button.config(font=("Arial", 14))
ramping_button.pack()






def difficulty_selected():
    global var2
    difficultylabel = Label(root, text="Difficulty: " + diffentry, bg="grey23", fg="white")
    difficultylabel.pack()
    easy_button.pack_forget()
    medium_button.pack_forget()
    hard_button.pack_forget()
    impossible_button.pack_forget()
    var2.set("play")

def difficulty_selected_easy():
    global diffentry
    diffentry = "EASY"
    difficulty_selected()

def difficulty_selected_medium():
    global diffentry
    diffentry = "MEDIUM"
    difficulty_selected()

def difficulty_selected_hard():
    global diffentry
    diffentry = "HARD"
    difficulty_selected()

def difficulty_selected_impossible():
    global diffentry
    diffentry = "IMPOSSIBLE"
    difficulty_selected()

easy_button = Button(root, text="Easy", command=difficulty_selected_easy, bg="grey8", fg="green2")
easy_button.config(font=("Arial", 14))
    
medium_button = Button(root, text="Medium", command=difficulty_selected_medium, bg="grey8", fg="goldenrod1")
medium_button.config(font=("Arial", 14))

hard_button = Button(root, text="Hard", command=difficulty_selected_hard, bg="grey8", fg="firebrick1")
hard_button.config(font=("Arial", 14))

impossible_button = Button(root, text="Impossible", command=difficulty_selected_impossible, bg="grey8", fg="DarkOrchid1")
impossible_button.config(font=("Arial", 14))

easy_button.wait_variable(var)
easy_button.pack()
medium_button.pack()
hard_button.pack()
impossible_button.pack()

label_color = "lime green"
color_selection = 0
snake_color = "lime green"


def color_options():
    global color_selection, snake_color, label_color
    color_selection = color_selection + 1
    if color_selection == 0:
        snake_color="lime green"
        label_color="lime green"
        color_button.config(fg=label_color)

    if color_selection == 1:
        snake_color="red"
        label_color="red"
        color_button.config(fg=label_color)

    if color_selection == 2:
        snake_color="deep sky blue"
        label_color="deep sky blue"
        color_button.config(fg=label_color)

    if color_selection == 3:
        snake_color="purple3"
        label_color="purple3"
        color_button.config(fg=label_color)

    if color_selection == 4:
        snake_color="orange"
        label_color="orange"
        color_button.config(fg=label_color)

    if color_selection == 5:
        snake_color="yellow"
        label_color="yellow"
        color_button.config(fg=label_color)

    if color_selection == 6:
        snake_color="cyan2"
        label_color="cyan2"
        color_button.config(fg=label_color)

    if color_selection == 7:
        color_selection = 0
        snake_color="lime green"
        label_color="lime green"
        color_button.config(fg=label_color)

color_button = Button(root, text="Snake Color", command=color_options, bg="grey8", fg=label_color)
color_button.config(font=("Arial", 14))


color_button.wait_variable(var2)
color_button.pack()
def start_game():
    var3.set("RUNDIFFICULTYANDGAMEMODE")
    root.destroy()

play_button = Button(root, text="PLAY", command=start_game, bg="grey23", fg="white",)
play_button.config(font=("Comic Sans MS", 15))

play_button.pack()
playgame=Button(root)
playgame.wait_variable(var3)


delay = int(125)

def delay_logic():
    global delay
    if diffentry == "EASY":
        delay = 150
    if diffentry == "MEDIUM":
        delay = 115
    if diffentry == "HARD":
        delay = 85
    if diffentry == "IMPOSSIBLE":
        delay = 50

delay_logic()

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def game_loop():
    player.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - width / 2 or new_head[0] > width / 2 \
            or new_head[1] < - height / 2 or new_head[1] > height / 2:
        reset()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Remove last segment of snake.
        if not food_collision():
            snake.pop(0)

        # Draw snake for the first time.
        for segment in snake:
            player.goto(segment[0], segment[1])
            player.stamp()

        # Refresh screen
        screen.title(f"Snake Game, Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, delay)

def food_collision():
    global food_pos, score, delay
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        if gmentry == "RAMPING DIFFICULTY":
            delay -= 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- width / 2 + food_size, width / 2 - food_size)
    y = random.randint(- height / 2 + food_size, height / 2 - food_size)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance

def reset():
    global score, snake, snake_direction, food_pos, delay
    score = 0
    delay_logic()
    snake = [[0,0],[20,0],[40,0],[60,0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

screen = turtle.Screen() #defining window resolution as "screen"
screen.setup(width, height) #setup window(screen) size with width and height variables

screen.title("Snake") #window name
screen.tracer(0)
turtle.Screen().bgcolor("grey18") #https://jjfiv.github.io/cs145-f2020/TkInterColorCharts.png

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")


#creating player
player = turtle.Turtle()
player.penup()
player.shape("square")
player.color("black", snake_color)




#creating player MODEL
snake = [[0,0],[20,0],[40,0],[60,0]]
snake_direction = "up"


food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.penup()
food.shapesize(food_size/20)
food_pos = get_random_food_pos()
food.goto(food_pos)



for segment in snake:
    player.goto(segment[0], segment[1])
    player.stamp()


reset() 

turtle.done()
