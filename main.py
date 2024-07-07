# necessary imports
import tkinter
import random

# function that reset the game
def reset():
    # resets the buttons to active state and empty text
    for i in range(size):
        for j in range(size):
            buttons[i][j]['text'] = ""
            buttons[i][j]['state'] = "active"

    # resets the global variables
    global player_current, number_of_tiles
    player_current = random.choice(players)
    number_of_tiles = size*size
    label['text'] = "Player "+ player_current +" turn"
    
    # changes the dimensions of the items in the window
    label.config(font=("Helvetica", window.winfo_height()//size//4))
    reset_button.config(width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))
    settings_button.config(width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))

# function that stops the game(disables the buttons)
def stop():
    for i in range(size):
        for j in range(size):
            buttons[i][j]['state'] = "disabled"

# function that checks if someone has won, checks all 8 directions, currently there is no way to change the number of tiles needed to win, will be added in the future
def check_for_win(x, y):
    # check for 8 directional wins
    if buttons[x][y]['text'] == player_current:
        # check for horizontal win
        for i in range(size):
            if buttons[x][i]['text'] != player_current:
                break
            if i == size-1:
                label['text'] = "Player " + player_current + " wins"
                return True
        # check for vertical win
        for i in range(size):
            if buttons[i][y]['text'] != player_current:
                break
            if i == size-1:
                label['text'] = "Player " + player_current + " wins"
                return True
        # check for diagonal win
        if x == y:
            for i in range(size):
                if buttons[i][i]['text'] != player_current:
                    break
                if i == size-1:
                    label['text'] = "Player " + player_current + " wins"
                    return True
        # check for anti diagonal win
        if x + y == size - 1:
            for i in range(size):
                if buttons[i][(size-1)-i]['text'] != player_current:
                    break
                if i == size-1:
                    label['text'] = "Player " + player_current + " wins"
                    return True
    return False

# function that changes the ownership of a button/tile
def change_ownership(x, y):
    global player_current, number_of_tiles
    if buttons[x][y]['text'] == "":
        buttons[x][y]['text'] = player_current
        if check_for_win(x, y):
            stop()
        else:
            if player_current == "X":
                player_current = "O"
            else:
                player_current = "X"
            number_of_tiles -= 1
    else:
        print("This tile is already taken")
    if number_of_tiles == 0:
        label['text'] = "Draw"

# function that creates a settings window
def settings_window():
    pass



# variables

# size of the tiles
pixelsize = 100
# size of the board
size = 3
# number of tiles needed to win
#winning_tiles = 3
# number of tiles in the board
number_of_tiles = size*size
# list of events
events = []

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
window.geometry("1200x700")
window.resizable(True, True)
window.iconbitmap("icon.ico")

# create the top label
label = tkinter.Label(window, text="Players: "+ player_current +" turn", font=("Helvetica", window.winfo_height()//size//4))
label.pack(side="top")


# create a frame for the buttons
frame = tkinter.Frame(window)
frame.pack(side="top")

# Create buttons, and place them in the window on a grid
for i in range(size):
    for j in range(size):
        buttons[i][j] = tkinter.Button(frame, text="", width=(size*2)*3, height=size*3, command=lambda row = i, collum = j: change_ownership(row,collum))
        buttons[i][j].grid(row=i, column=j)

# creating a frame for the special buttons
game_buttons = tkinter.Frame(window)
game_buttons.pack(side="bottom")

# create the reset button
reset_button = tkinter.Button(game_buttons, text="Reset", command=reset, width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))
reset_button.grid(row=0, column=0)

# creating a settings menu button
settings_button = tkinter.Button(game_buttons, text="Settings", command=lambda: settings_window(), width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))
settings_button.grid(row=0, column=1)

window.mainloop()
