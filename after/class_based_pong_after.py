'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle

class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position

        self.turt = make_turtle("square", "white", 5, 1, self.x_position, self.y_position)

        
    def up(self):
        ''' Move paddle up '''
        y = self.turt.ycor()
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        self.turt.sety(y)    #move the paddle to the new y position
        self.y_position = y
    

    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()



class Ball:
    # implements a Pong game ball

    def __init__(self, speed_x = 0.0925, speed_y = 0.0925):
        ''' intializes a ball with default direction and position '''

        self.turt = make_turtle("square", "white", 1, 1, 0, 0)
        self.ball_dx = speed_x #speed in x direction
        self.ball_dy = speed_y #speed in y direction
        self.x_position = 0
        self.y_position = 0

    
    def move(self):
        ''' moves the ball in x and y directions '''

        # Move the ball
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()
        self.checkBound()
    
        
    def checkBound(self):
        # Top and bottom
        if self.turt.ycor() > 290:
            self.turt.sety(290)
            self.ball_dy *= -1

        elif self.turt.ycor() < -290:
            self.turt.sety(-290)
            self.ball_dy *= -1
    
    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()


    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


    def setx(self, x_cor):
        ''' sets the ball x position '''
        self.turt.setx(x_cor)
        self.x_position = x_cor



def make_window(window_title, bgcolor, width, height):
    '''this function creates a screen object and returns it'''

    window = turtle.getscreen() #Set the window size
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0) #turns off screen updates for the window Speeds up the game
    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0) # Speed of animation, 0 is max
    turt.shape(shape) # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) #Start position
    return turt

class Player:
    def __init__(self, x_position, y_position):
        self.score = 0
        self.paddle = Paddle(x_position, y_position)
    def addScore(self):
        self.score += 1
    def getScore(self):
        return self.score

class Game:
    def __init__(self, ball_x = 0.0925, ball_y = 0.0925):
        self.window = make_window("Pong - A CS151 Reproduction!", "black", 800, 600)
        self.player1 = Player(-350, 0)
        self.player2 = Player(350, 0)
        self.ball = Ball(ball_x, ball_y)
        self.pen = make_turtle("square", "white", 1, 1, 0, 260)

    def scoreBoard(self):
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
        self.pen.hideturtle()

    def keyBoard(self):
        self.window.listen() #Listen for keyboard input
        self.window.onkeypress(self.player1.paddle.up, "w") #when you press w run paddle_a_up
        self.window.onkeypress(self.player1.paddle.down, "s")
        self.window.onkeypress(self.player2.paddle.up, "Up")
        self.window.onkeypress(self.player2.paddle.down, "Down")
    
    def play(self):
        self.scoreBoard()
        self.keyBoard()
        while True:
            self.window.update()
            self.ball.move()
            self.borderCheck()
            self.collision()

    def borderCheck(self):
        # Border checking    
        # Left and right
        if self.ball.xcor() > 350:
            self.player1.addScore()
            self.resetBall()

        elif self.ball.xcor() < -350:
            self.player2.addScore()
            self.resetBall()

    def resetBall(self):
        self.pen.clear()
        self.pen.write("Player A: "+ str(self.player1.getScore()) + "  Player B: "+ str(self.player2.getScore()), align="center", font=("Courier", 24, "normal"))
        self.ball.goto(0, 0)
        self.ball.ball_dx *= -1

    def collision(self):
        if self.collide_player(1):
            self.ball.setx(-340)
            self.ball.ball_dx *= -1.5
        
        elif self.collide_player(2):
            self.ball.setx(340)
            self.ball.ball_dx *= -1.5

    def collide_player(self,player):
        if(player == 1):
            return self.ball.xcor() < -340 and self.ball.xcor() > -350 and self.ball.ycor() < self.player1.paddle.ycor() + 50 and self.ball.ycor() > self.player1.paddle.ycor() - 50
        elif(player == 2):
            return self.ball.xcor() > 340 and self.ball.xcor() < 350 and self.ball.ycor() < self.player2.paddle.ycor() + 50 and self.ball.ycor() > self.player2.paddle.ycor() - 50

def main():
    g = Game(0.5,0.5)
    g.play()




if __name__ == "__main__":
	main()