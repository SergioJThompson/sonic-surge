from tkinter import *
from tkinter.ttk import *
from pygame import mixer


def open_root_window():
    root = Tk()
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")

    place_button(root, "Play mp3", mixer.Sound("coin.mp3").play, 100, 50)
    place_button(root, "Choose an mp3", mixer.Sound("boom.mp3").play, 85, 90)


def place_button(window, text, command, x, y):
    btn = Button(window, text=text, command=command)
    btn.place(x=x, y=y)
    # TODO: set default x coord to (center divided by two minus half of width) based on input width


def main():
    mixer.init()
    open_root_window()
    mainloop()


main()
