from tkinter import *
from tkinter import font
from tkinter import filedialog

from os.path import expanduser

from simpleaudio import WaveObject
from pydub import AudioSegment

from MsgLibrary import MsgLibrary
from SoundMemoryBank import SoundMemoryBank
from TextFitter import TextFitter
from SoundBuilder import SoundBuilder
from SoundPlayer import SoundPlayer
from WidgetLibrary import WidgetLibrary as widgetlib
from Sound import Sound


# TODO: Implement new classes and remove the old stuff


def create_root_window():
    root = Tk()
    window_width = 302
    window_height = 120
    root.minsize(window_width, window_height)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")
    return root


def create_widget_pairs(window, msgs, builder, player):
    widget_pairs = {}

    widget_pairs.add("file loaded lbl", Label(window, text=msgs.no_file_loaded_txt(), justify=CENTER))
    widget_pairs.add("reversed lbl", Label(window, justify=CENTER))

    file_loaded_lbl = widget_pairs.get("file loaded lbl")

    widget_pairs.add("play btn", Button(window, text=msgs.play_button_txt(), command=player.play))
    widget_pairs.add("choose btn", Button(window, text=msgs.choose_button_txt(),
                                          command=lambda: stop_playback_and_load_file(player, file_loaded_lbl)))
    widget_pairs.add("stop btn", Button(window, text=msgs.stop_btn_txt(), command=lambda: player.stop()))
    widget_pairs.add("reverse btn)", Button(window, text=msgs.reverse_btn_txt(),
                                            command=lambda: reverse_file(builder, file_loaded_lbl)))

    return widget_pairs


def root_widgets_to_grid(file_loaded_lbl, reversed_lbl, choose_btn, play_btn, reverse_btn, stop_btn):
    file_loaded_lbl.grid(row=0, column=0, columnspan=3)
    reversed_lbl.grid(row=1, column=0, columnspan=3)
    choose_btn.grid(row=2, column=1)
    play_btn.grid(row=3, column=0)
    reverse_btn.grid(row=3, column=1)
    stop_btn.grid(row=3, column=2)


def root_grid_config(root):
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)


def stop_playback_and_load_file(player, file_loaded_lbl):
    player.stop_if_playing()

    path = get_file_path_from_user()

    if path:  # If user didn't click cancel
        SoundPlayer.sound = SoundBuilder.build_sound_from_path(Sound(), path)
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


def get_file_name_from_path(path):      # TODO: Move this and other functions to TextFitte
                                        # TODO: rename it TextFormatter
    return path[path.rfind("/") + 1:]


def seg_to_wave_obj(seg: AudioSegment):
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def reverse_file(file_mgr, reversed_lbl):
    if file_mgr.path:
        seg = AudioSegment.from_file(file_mgr.path).reverse()
        file_mgr.build_sound_parts_from_audio_seg(seg)
        change_reversed_file_lbl_txt(reversed_lbl)

    # TODO: Move this function to FileHandler
    # TODO: Save reversed file as FileHandler.reversed_wave_obj for easy access to both reversed and unreversed file


def change_reversed_file_lbl_txt(reversed_lbl):
    if not reversed_lbl.cget("text"):
        reversed_lbl.config(text="Reversed file!")
    else:
        reversed_lbl.config(text="")


def main():
    msgs = MsgLibrary()
    builder = SoundBuilder()
    memory = SoundMemoryBank()
    player = SoundPlayer()
    txt_fitter = TextFitter()
    root = create_root_window()

    widgetlib.widgets = create_widget_pairs(root, msgs, builder, player)

    mainloop()


main()
