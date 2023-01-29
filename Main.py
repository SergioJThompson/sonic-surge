from tkinter import *
from tkinter import font
from tkinter import filedialog
from os.path import expanduser
from simpleaudio import WaveObject

from Playbutton import Playbutton
from pydub import AudioSegment
from MsgLibrary import MsgLibrary
from FileMemory import FileMgr
from TextFitter import TextFitter

# TODO: reassign file-remembering responsibility from Playbutton to FileMemory
# TODO: why playback freezes or just does nothing when you hit play for the second time?


def create_root_window_and_widgets():
    root = Tk()
    window_width = 302
    window_height = 120
    root.minsize(window_width, window_height)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")

    file_mgr = FileMgr
    msgs = MsgLibrary

    play_btn = Playbutton(root, text=msgs.play_button_txt())
    choose_btn = Button(root, text=msgs.choose_button_txt(),
                        command=lambda: load_file(play_btn, file_loaded_lbl, file_mgr))
    stop_btn = Button(root, text=msgs.stop_btn_txt(),
                      command=lambda: play_btn.stop())
    reverse_btn = Button(root, text=msgs.reverse_btn_txt(),
                         command=lambda: reverse_file(play_btn, reversed_lbl, file_mgr))

    file_loaded_lbl = Label(root, text=msgs.no_file_loaded_txt(), justify=CENTER)
    reversed_lbl = Label(root, justify=CENTER)

    file_loaded_lbl.grid(row=0, column=0, columnspan=3)
    reversed_lbl.grid   (row=1, column=0, columnspan=3)
    choose_btn.grid     (row=2, column=1)
    play_btn.grid       (row=3, column=0)
    reverse_btn.grid    (row=3, column=1)
    stop_btn.grid       (row=3, column=2)

    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)

    # TODO: make label text change responsively when window size increased/decreased


def load_file(play_btn, file_loaded_lbl, file_mgr):
    play_btn.stop()
    path = get_file_path_from_user()
    file_mgr.path_to_file = path
    if path != '':
        play_btn.set_sound(get_wave_object_from_path(path))
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


def get_wave_object_from_path(audio_file_path):
    seg = AudioSegment.from_file(audio_file_path)
    return seg_to_wave_obj(seg)


def seg_to_wave_obj(seg):
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def reverse_file(play_btn, reversed_lbl, file_mgr):
    seg = AudioSegment.from_file(file_mgr.path_to_file).reverse()
    play_btn.set_sound(seg_to_wave_obj(seg))

    change_reversed_file_lbl_txt(reversed_lbl)


def change_reversed_file_lbl_txt(reversed_lbl):
    if not reversed_lbl.cget("text"):
        reversed_lbl.config(text="Reversed file!")
    else:
        reversed_lbl.config(text="")


def main():
    create_root_window_and_widgets()
    mainloop()


main()

# TODO: pause button
# TODO: backwards audio button!
