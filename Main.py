from tkinter import *
from tkinter import font
from tkinter import filedialog
from os.path import expanduser
from simpleaudio import WaveObject
from Playbutton import Playbutton
from pydub import AudioSegment
from MsgLibrary import MsgLibrary
from TextFitter import TextFitter


def create_root_window():
    root = Tk()
    window_width = 302
    window_height = 50
    root.minsize(window_width, window_height)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")

    msgs = MsgLibrary

    play_btn = Playbutton(root, text=msgs.play_button_txt())
    choose_btn = Button(root, text=msgs.choose_button_txt(), command=lambda: change_file(play_btn, file_loaded_lbl))

    file_loaded_lbl = Label(root, text="No file loaded.", justify=CENTER)
    invis_lbl1 = Label(root)
    invis_lbl2 = Label(root, width=10)

    file_loaded_lbl.grid(column=0, row=0, columnspan=3)
    invis_lbl1.grid(column=0, row=1, columnspan=3)

    play_btn.grid(column=0, row=2)
    invis_lbl2.grid(column=1, row=2)
    choose_btn.grid(column=2, row=2)

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)

    # TODO: make label text change responsively when window size increased/decreased


def change_file(play_btn, file_loaded_lbl):
    play_btn.stop()
    path = get_file_path_from_user()
    if path != '':
        play_btn.set_sound(get_wave_object(path))
        file_name = get_file_name_from_path(path)
        file_loaded_lbl.config(text=file_loaded_msg(file_name, file_loaded_lbl))


def get_file_path_from_user():
    return filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])


def file_loaded_msg(file_name, lbl):
    txt = MsgLibrary.file_loaded_msg_first_part() + file_name
    txt_font = font.nametofont(lbl.cget("font"))
    window_width = lbl.master.winfo_width()
    txt = TextFitter.truncate_as_far_as_necessary_or_possible_to_fit_in_window(txt, txt_font, window_width)
    return txt


def get_file_name_from_path(path):
    return path[path.rfind("/")+1:]


def get_wave_object(audio_file_path):
    seg = AudioSegment.from_file(audio_file_path)
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def main():
    create_root_window()
    mainloop()


main()

# TODO: pause button
# TODO: backwards audio button!
