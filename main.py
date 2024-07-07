# necessary imports
import tkinter
import random

# function that reset the game
def reset():
    for i in range(size):
        for j in range(size):
            buttons[i][j]['text'] = ""

# function that checks if someone has won
def check_for_win():
    pass

# function that checks if the board is full, if yes than its a draw
def check_if_tiles():
    if number_of_tiles == 0:
        label['text'] = "Draw"
    else:
        pass

# function that changes the ownership of a button/tile
def change_ownership(x, y):
    global player_current, number_of_tiles
    if buttons[x][y]['text'] == "":
        buttons[x][y]['text'] = player_current
        if player_current == "X":
            player_current = "O"
        else:
            player_current = "X"
        number_of_tiles -= 1
    else:
        print("This tile is already taken")

# variables that set the size of the game and of the buttons, and a variable that sets how many tiles are needed to win, and a variable that tells how many free tiles there are
pixelsize = 100
size = 3
winning_tiles = 3
number_of_tiles = size*size

# create the window variables, and the all the global variables
windowheight = int(pixelsize * size)
windowwidth = int(pixelsize * size)
players = ["X", "O"]
player_current = random.choice(players)
buttons =[]
for i in range(size):
    buttons.append([])
    for j in range(size):
        buttons[i].append([])

# window setings
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.geometry("500x500")
window.resizable(False, False)
#window.iconbitmap("icon.ico")

# create a frame for the buttons
frame = tkinter.Frame(window)
frame.pack(side="top")

# create the reset button
reset_button = tkinter.Button(window, text="Reset", command=reset, width=10, height=2)
reset_button.pack(side="bottom")

# Create buttons, and place them in the window on a grid
for i in range(size):
    for j in range(size):
        buttons[i][j] = tkinter.Button(frame, text="", width=(size*2)*3, height=size*3, command=lambda row = i, collum = j: change_ownership(row,collum))
        buttons[i][j].grid(row=i, column=j)
        print("Button at: ", i, j)

# create the top label
label = tkinter.Label(window, text="Player"+ player_current +"turn")
label.pack(side="top")




window.mainloop()