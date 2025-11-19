import turtle
import time
import random

# --- Configuration de la fenêtre ---
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# --- Création de la tête du serpent ---
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

# --- Création de la nourriture ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# --- Création du stylo pour le score / messages ---
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()

game_over = False

# --- Fonctions de direction ---
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# --- Mouvement du serpent ---
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# --- Réinitialiser le jeu après Game Over ---
def reset_game():
    global game_over, segments
    if game_over:
        # Remettre la tête au centre et stopper le mouvement
        head.goto(0, 0)
        head.direction = "stop"

        # Cacher et vider les segments
        for seg in segments:
            seg.hideturtle()
        segments.clear()

        # Effacer le message "GAME OVER"
        pen.clear()

        # Remettre le drapeau à False
        game_over = False

# --- Contrôles clavier ---
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(reset_game, "space")  # relancer le jeu avec Espace

# --- Boucle principale ---
while True:
    wn.update()
    
    if not game_over:
        # Collision avec les murs
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            pen.goto(0, 0)
            pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            game_over = True

        # Collision avec la nourriture
        if head.distance(food) < 20:
            food.goto(random.randint(-14, 14)*20, random.randint(-14, 14)*20)

            # Ajouter un segment
            seg = turtle.Turtle()
            seg.shape("square")
            seg.color("green")
            seg.penup()
            segments.append(seg)

        # Déplacement des segments
        for i in range(len(segments)-1, 0, -1):
            segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Collision avec soi-même
        for seg in segments:
            if head.distance(seg) < 20:
                pen.goto(0, 0)
                pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
                game_over = True
                break

    time.sleep(0.1)
