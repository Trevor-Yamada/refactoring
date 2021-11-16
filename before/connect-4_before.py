'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

import turtle
#REFACTORED
x_offset = -150
y_offset = 200
tile_size = 50
turn = 1
grid = [] #MOVED HERE
turns = 0

def make_window(window_title, bgcolor, shape):#REFACTORED
	''' this function creates a screen object and returns it '''

	window = turtle.getscreen() # Set the window size
	window.title(window_title)
	window.bgcolor(bgcolor)
	window.setup(*shape)#REFACTORED
	window.tracer(0) #turns off screen updates for the window Speeds up the game
	return window


def make_turtle(shape, color, stretch, pos):#REFACTORED
    ''' creates a turtle and sets initial position '''
    turt = turtle.Turtle()
    turt.speed(0)    # Speed of animation, 0 is max
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(*stretch) #REFACTORED
    turt.penup()
    turt.goto(*pos) # Start position #REFACTORED
    return turt


def draw_grid(grid, turt, x_pos, y_pos, tile_size):
    ''' draws a grid at x, y with a specific tile_size '''

    place_turtle(turt,(x_pos,y_pos))#REFACTORED

    for row in range(len(grid)):
        for col in range(len(grid[row])):
        
            place_turtle(turt,(x_pos + col * tile_size, y_pos -row * tile_size)) #REFACTORED
            draw_dot( turt ,tile_size, grid[row][col])#REFACTORED

def place_turtle(turt, pos): #REFACTORED
    turt.up()
    turt.goto(*pos)
    turt.down()

def draw_dot( turt, tile_size, player): #REFACTORED
    player_color = {1 : "red", 2 : "yellow", 0 : "white"}
    turt.dot(tile_size-5, player_color[player])

def check_win(grid, player):
    #REFACTORED COMMENT
    ''' checks the winner in the grid
    returns true if player won
    returns false if player hasnt won...yet
     '''

    count = 0

    # check rows
    for row in range(len(grid)):
        count = 0
        for col in range(len(grid[0])):
            if grid[row][col] == player:
                count += 1

                if count == 4:
                    return True
            else:
                count = 0
            
    # check columns
    for col in range(len(grid[0])):
        count = 0
        for row in range(len(grid)):
            if grid[row][col] == player:
                count += 1
                
                if count == 4:
                    return True
            else:
                count = 0

    # check for diagonal 4 
    #REFACTORED
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if row + 3 < len(grid) and col + 3 < len(grid[row]):
                #Decending diagonal check
                if grid[row][col] == player\
                   and grid[row+1][col+1] == player\
                   and grid[row+2][col+2] == player\
                   and grid[row+3][col+3] == player:
                   return True

            if row + 3 < len(grid) and col - 3 >= 0: 
                #Acending diagonal check
                if grid[row][col] == player\
                   and grid[row+1][col-1] == player\
                   and grid[row+2][col-2] == player\
                   and grid[row+3][col-3] == player:
                   return True
            



# setting up the window
window = make_window("Connect 4", "light sky blue", (800, 600))

#Moved grid[] to global variable
#Moved grid creation to main() function 

# drawing_turtle
my_turtle = make_turtle('classic', "white",( 1, 1), (0, 0))

def play(x_pos,y_pos):
    ''' '''
    global turn
    global turns #created global variable to keep track of CATS GAME(No winners) Status

    
    col = int(abs((x_pos - x_offset - 25) // (50) + 1))
    
    #variable to index each column 
    i = (len(grid)-1)
    while i != 5 : #REFACTORED TO INCLUDE "GRAVITY" LIKE THE REAL CONNECT 4
        if grid[i][col] == 0:
            grid[i][col] = turn
            i = 5
        else:
            i -= 1
    
    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)
    window.update()

    if check_win(grid, 1):
        print("player 1 won")

    elif check_win(grid, 2):
        print("player 2 won")
    
    #Turn-change and Cats game Checker
    if turn == 1:
        turn = 2
        turns+=1
        if turns == 35:#if board is filled
            print('CATS GAME')
            window.exitonclick()
    else:
        turn = 1
        turns += 1
    


def main():
    ''' the main function where the game events take place '''
    for rows in range(5):#REFACTORED
        grid.append([0]*7)
    
    window.onscreenclick(play)#REFACTORED
    window.listen()

    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)

    while True:
        window.update()

if __name__ == "__main__":
	main()

