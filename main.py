# necessary imports
import tkinter
import random

# function that reset the game
def reset():
    global buttons, size, player_current, number_of_tiles, pixelsize, frame, settings_button, reset_button, label, players
    #buttons.clear()
    # destroys the old buttons from the frame in window in order to create new ones
    for widget in frame.winfo_children():
        widget.destroy()
#    print(oldsize)
#    print(pixelsize)
#    if pixelsize != oldsize:
#    for i in range(size):
#        for j in range(size):
#            print("destroying")
#            print(buttons[i][j])
#            buttons[i][j].destroy()
#            print(buttons[i][j])
#            print("destroyed")
    buttons.clear()
    # addapts the changes to the number of buttons
    for i in range(size):
        buttons.append([])
        for j in range(size):
            buttons[i].append([])
            #print(buttons[i][j])
            
    #print(size)
    # creates the new buttons
    create_buttons(size)

    # resets the buttons to active state and empty text and change their size
    # with and height of the buttons is determined by a percalage of the window size
    buttons_width = window.winfo_height()/size/10
    buttons_height = buttons_width/2
    # the font size is determined by the size of a button
    #buttons_font = buttons_width//2
    #print(window.winfo_height())
    #print(window.winfo_width())
    #print(buttons_width)
    #print(buttons_height)

    try:
        for i in range(size):
            for j in range(size):
                buttons[i][j]['text'] = ""
                buttons[i][j]['state'] = "active"
                buttons[i][j].config(width=int(buttons_width), height=int(buttons_height))
    except TypeError:
        pass

    # resets the global variables
    player_current = random.choice(players)
    number_of_tiles = size*size
    label['text'] = "Player "+ player_current +" turn"
    
    # changes the dimensions of the items in the window
    label.config(font=("Helvetica", window.winfo_height()//size//4))
    reset_button.config(width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))
    settings_button.config(width=int(window.winfo_width()/size/10), height=int(window.winfo_height()/size/10/4))
    # changes the dimensions of the frame to accomodate the new button size
    frame.config(width=size*pixelsize, height=size*pixelsize/2)

# function that stops the game(disables the buttons)
def stop():
    global buttons, size
    for i in range(size):
        for j in range(size):
            buttons[i][j]['state'] = "disabled"

# function that checks if someone has won, checks all 8 directions, 
# works for any size of the board, 
# this function needs to check every button every time a button is pressed, this is not optimal, but it works
# the function checks the surrounding buttons of the button that was pressed, and if they are the same as the button that was pressed, it checks the next one, and so on
def check_for_win():
    global player_current, buttons, label, winning_tiles, size
    for i in range(size):
        for j in range(size):
            if buttons[i][j]['text'] == player_current:
                # check for horizontal win
                for k in range(winning_tiles):
                    if j + k < size:
                        if buttons[i][j+k]['text'] != player_current:
                            break
                        if k == winning_tiles-1:
                            label['text'] = "Player " + player_current + " wins"
                            return True
                # check for vertical win
                for k in range(winning_tiles):
                    if i + k < size:
                        if buttons[i+k][j]['text'] != player_current:
                            break
                        if k == winning_tiles-1:
                            label['text'] = "Player " + player_current + " wins"
                            return True
                # check for diagonal win
                for k in range(winning_tiles):
                    if i + k < size and j + k < size:
                        if buttons[i+k][j+k]['text'] != player_current:
                            break
                        if k == winning_tiles-1:
                            label['text'] = "Player " + player_current + " wins"
                            return True
                # check for anti diagonal win
                for k in range(winning_tiles):
                    if i + k < size and j - k >= 0:
                        if buttons[i+k][j-k]['text'] != player_current:
                            break
                        if k == winning_tiles-1:
                            label['text'] = "Player " + player_current + " wins"
                            return True
    return False

# function that changes the ownership of a button/tile
def change_ownership(x, y):
    global player_current, number_of_tiles, players
    if buttons[x][y]['text'] == "":
        buttons[x][y]['text'] = player_current
        if check_for_win():
            stop()
        else:
            if player_current == players[0]:
                player_current = players[1]
            else:
                player_current = players[0]
            number_of_tiles -= 1
            label['text'] = "Player "+ player_current +" turn"
    else:
        print("This tile is already taken")
    if number_of_tiles == 0:
        label['text'] = "Draw"


# function that applies the settings
def apply_settings(size_entry, winning_tiles_entry, resizable_option):
    global size, pixelsize, winning_tiles, resizable
    # try to aplly the settings
    try:
        # checks if the values are valid
        if int(winning_tiles_entry) <= 2 or int(winning_tiles_entry) > int(size_entry) or int(size_entry) < 3 or int(size_entry) > 15 :
            return
        else:
            # changes the values of the global variables
            size = int(size_entry)
            #pixelsize = int(tiles_size_entry)
            winning_tiles = int(winning_tiles_entry)
            # changes the window settings
            window.resizable(resizable_option, resizable_option)
            if resizable_option == 0:
                resizable = 0
            # resets the game to apply the changes
            reset()
    except:
        pass




# function that creates a settings window
def settings_window():
    global size, pixelsize, winning_tiles, resizable
    # the settings window and the title, geometry, and icon
    settings = tkinter.Toplevel(window)
    settings.title("Settings")
    settings.geometry("400x300")
    settings.resizable(False, False)
    settings.iconbitmap("icon.ico")
    # main label
    settings_label = tkinter.Label(settings, text="Settings", font=("Helvetica", 20))
    settings_label.pack(side="top")
    # the frame for the settings
    settings_frame = tkinter.Frame(settings)
    settings_frame.pack(side="top")
    # size of the board label and entry
    size_label = tkinter.Label(settings_frame, text="Size of the board: ")
    size_label.grid(row=0, column=0)
    e1 = tkinter.StringVar()
    e1.set(size)
    size_entry = tkinter.Entry(settings_frame, textvariable=e1)
    size_entry.grid(row=0, column=1)
    recomended_size_label = tkinter.Label(settings_frame, text="Range is: 3-15")
    recomended_size_label.grid(row=0, column=2)
    # size of the tiles label and entry
    #tiles_size_label = tkinter.Label(settings_frame, text="Size of the tiles: ")
    #tiles_size_label.grid(row=1, column=0)
    #e2 = tkinter.StringVar()
    #e2.set(pixelsize)
    #tiles_size_entry = tkinter.Entry(settings_frame, textvariable=e2)
    #tiles_size_entry.grid(row=1, column=1)
    # tiles needed to win label and entry
    winning_tiles_label = tkinter.Label(settings_frame, text="Tiles needed to win: ")
    winning_tiles_label.grid(row=2, column=0)
    e3 = tkinter.StringVar()
    e3.set(winning_tiles)
    winning_tiles_entry = tkinter.Entry(settings_frame, textvariable=e3)
    winning_tiles_entry.grid(row=2, column=1)
    recomended_winning_tiles_label = tkinter.Label(settings_frame, text="Range is: 3-15")
    recomended_winning_tiles_label.grid(row=2, column=2)
    # resizable window option
    var = tkinter.IntVar()
    var.set(resizable)
    resizable_label = tkinter.Label(settings_frame, text="Resizable window: ")
    resizable_label.grid(row=3, column=0)
    resizable_option = tkinter.Checkbutton(settings_frame, variable=var)
    resizable_option.grid(row=3, column=1)
    # apply button
    apply_button = tkinter.Button(settings, text="Apply", command=lambda: apply_settings(size_entry.get(), winning_tiles_entry.get(), var.get()))
    apply_button.pack(side="bottom")
    # note label
    note_label = tkinter.Label(settings, text="Note: The changes will be applied only if they are within the specified range")
    note_label.pack(side="bottom")


# function that creates the buttons
def create_buttons(size):
    global buttons, pixelsize, frame
    for i in range(size):
        for j in range(size):
            buttons[i][j] = tkinter.Button(frame, text="", width=int(pixelsize), height=int(pixelsize/2), command=lambda row = i, collum = j: change_ownership(row,collum))
            buttons[i][j].grid(row=i, column=j)
    #print(buttons)
    #print(len(buttons))
    #print(len(buttons[0]))
    #print(len(buttons[1]))
    #print(len(buttons[2]))


# variables

# initial size of the tiles
pixelsize = 22
# size of the board
size = 3
# number of tiles needed to win
winning_tiles = 3
# number of tiles in the board
number_of_tiles = size*size
# list of events
events = []

# create the window variables, and the all the global variables
windowheight = int(pixelsize * size)
windowwidth = int(pixelsize * size)
players = ["1", "0"]
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
resizable = 1
window.iconbitmap("icon.ico")

# create the top label
label = tkinter.Label(window, text="Player: "+ player_current +" turn", font=("Helvetica", window.winfo_height()//size//4))
label.pack(side="top")


# create a frame for the buttons
frame = tkinter.Frame(window, width=size*pixelsize, height=size*pixelsize/2)
frame.pack(side="top")

# Create buttons is now in a function, this is because of the settings window
create_buttons(size)


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
