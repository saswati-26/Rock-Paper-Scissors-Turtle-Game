import turtle
import random

#function for updating or adding scores of player
def update_player_score():
    global player_score
    player_score+=1
    player_pen.clear()
    style=("Arial",20,"bold")
    player_pen.write(f"You: {player_score}", align="center", font=style)

#function for updating or adding scores of computer
def update_computer_score():
    global computer_score
    computer_score+=1
    computer_pen.clear()
    style=("Arial",20,"bold")
    computer_pen.write(f"Computer: {computer_score}", align="center", font=style)
    
#defining function according to game condition
def rock():    
    player.shape(rock_img)
    choice=random.randint(0,2)
    computer.shape(possible_choices[choice])

    if choice==1: #computer chose paper
        update_computer_score()
    elif choice==2: #computer chose scissors
        update_player_score()
    

def paper():
    player.shape(paper_img)
    choice=random.randint(0,2)
    computer.shape(possible_choices[choice])

    if choice==0: #computer chose rock
        update_player_score()
    elif choice==2: #computer chose scissors
        update_computer_score()

def scissors():
    player.shape(scissors_img)
    choice=random.randint(0,2)
    computer.shape(possible_choices[choice])

    if choice==0: #computer chose rock
        update_computer_score()
    elif choice==1: #computer chose paper
        update_player_score()

#creating window using turtle
sc = turtle.Screen()
sc.bgcolor("DeepSkyBlue4")
sc.setup(width=1000,height=700)
sc.title("Rock-Paper-Scissors Game")

#create turtle object or variable
t=turtle.Turtle()

#draw partitioning
t.speed(0)
t.up()
t.left(90)
t.forward(500)
t.right(180)
t.down()
t.pensize(4)
t.color("white")
t.forward(1000)

#register images
rock_img="rock.gif"
paper_img="paper.gif"
scissors_img="scissors.gif"

possible_choices=[rock_img,paper_img,scissors_img]

turtle.register_shape(rock_img)
turtle.register_shape(paper_img)
turtle.register_shape(scissors_img)

#create player turtle
player=turtle.Turtle()
player.shape(rock_img)
player.up()
player.speed(0)
player.setposition(-280,-90)

#craete computer turtle
computer=turtle.Turtle()
computer.shape(rock_img)
computer.up()
computer.speed(0)
computer.setposition(280,-90)

#taking input from keyboard
turtle.listen()
turtle.onkeypress(rock,'r')
turtle.onkeypress(paper,'p')
turtle.onkeypress(scissors,'s')

#initialize scores
player_score=0
computer_score=0

#player score board
player_pen=turtle.Turtle()
player_pen.speed(0)
player_pen.up()
player_pen.hideturtle()
player_pen.goto(-250,250)
player_pen.color("white")
style=("Arial",20,"bold")
player_pen.write("You: 0",align="center", font=style)

#computer score board
computer_pen=turtle.Turtle()
computer_pen.speed(0)
computer_pen.up()
computer_pen.hideturtle()
computer_pen.goto(250,250)
computer_pen.color("white")
style=("Arial",20,"bold")
computer_pen.write("Computer: 0",align="center", font=style)



