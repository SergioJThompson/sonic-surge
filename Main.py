from tkinter import *
from tkinter import filedialog
from os.path import expanduser


from pygame import mixer
from PlayButton import PlayButton


def create_root_window():
    root = Tk()
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")

    sound = "coin.mp3"
    play_btn = PlayButton(sound, root, text="Play mp3", command=mixer.Sound(sound).play)
    choose_btn = Button(root, text="Choose mp3", command=lambda: choose_new_play_btn_sound(play_btn))
    play_btn.place(x=11, y=160)
    choose_btn.place(x=171, y=160)


def choose_new_play_btn_sound(play_btn):
    play_btn.sound = get_mp3_file_path_by_opening_finder_at_music_folder()


def get_mp3_file_path_by_opening_finder_at_music_folder():
    return filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])


def main():
    mixer.init()
    create_root_window()
    mainloop()


main()
