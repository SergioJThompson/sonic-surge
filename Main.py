from tkinter import *
from tkinter import filedialog

from os.path import expanduser

from simpleaudio import WaveObject
from pydub import AudioSegment

from MsgLibrary import MsgLibrary as Msgs
from SoundDict import SoundDict
from TextEditor import TextEditor
from SoundBuilder import SoundBuilder
from SoundPlayer import SoundPlayer
from WidgetDict import WidgetDict


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


def make_widget_dict(window):
    widget_pairs = {
        "file loaded lbl":
            Label(window, text=Msgs.no_file_loaded_txt(), justify=CENTER),
        "reversed lbl":
            Label(window, justify=CENTER),
        "play btn":
            Button(window, text=Msgs.play_button_txt(), command=SoundPlayer.play),
        "choose btn":
            Button(window, text=Msgs.choose_button_txt(), command=lambda: stop_playback_and_load_file_and_update_label()),
        "stop btn":
            Button(window, text=Msgs.stop_btn_txt(), command=lambda: SoundPlayer.stop_if_playing()),
        "reverse btn":
            Button(window, text=Msgs.reverse_btn_txt(), command=lambda: reverse_file_and_update_label())
    }
    return widget_pairs


def root_widgets_to_grid(widgets):
    widgets["file loaded lbl"]  .grid(row=0, column=0, columnspan=3)
    widgets["reversed lbl"]     .grid(row=1, column=0, columnspan=3)
    widgets["choose btn"]       .grid(row=2, column=1)
    widgets["play btn"]         .grid(row=3, column=0)
    widgets["reverse btn"]      .grid(row=3, column=1)
    widgets["stop btn"]         .grid(row=3, column=2)


def root_grid_config(root):
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)


def stop_playback_and_load_file_and_update_label():
    SoundPlayer.stop_if_playing()

    path = get_file_path_from_user()
    if path:  # If user didn't click cancel
        sound = SoundBuilder.build_sound_from_path(path)
        SoundDict.add("original", sound)
        SoundPlayer.sound = sound

        file_name = TextEditor.get_file_name_from_path(path)
        reversed_lbl = WidgetDict.widgets["reversed lbl"]
        fit_name = TextEditor.write_file_loaded_msg(file_name, reversed_lbl)
        reversed_lbl.config(text=fit_name)


def get_file_path_from_user():
    return filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])


def seg_to_wave_obj(seg: AudioSegment):
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def reverse_file_and_update_label():
    if "original" in SoundDict.sounds:
        seg = AudioSegment.from_file(SoundDict.sounds["original"].path).reverse()
        SoundBuilder.build_sound_from_audio_seg(seg)
        change_reversed_file_lbl_txt(WidgetDict.widgets["reversed lbl"])


def change_reversed_file_lbl_txt(reversed_lbl):
    if not reversed_lbl.cget("text"):
        reversed_lbl.config(text="Reversed file!")
    else:
        reversed_lbl.config(text="")


def main():
    root = create_root_window()
    WidgetDict.widgets = make_widget_dict(root)
    root_widgets_to_grid(WidgetDict.widgets)
    mainloop()


main()
