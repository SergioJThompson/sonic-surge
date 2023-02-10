# TODO: Fix labels not updating when you load a file, etc. Implement unit tests for this.

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
from WidgetNames import WidgetNames


def create_root_window():
    root = Tk()
    window_width = 244
    window_height = 123
    root.minsize(window_width, window_height)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")
    return root


def fill_widget_dict(window, player, sound_dict):
    sounds = sound_dict.sounds

    lbl_file_loaded = Label(window, text=Msgs.no_file_loaded_txt(), justify=CENTER, font='helvetica 14 bold')
    lbl_action = Label(window, justify=CENTER, font='helvetica 14')
    btn_play = Button(window, text=Msgs.play_button_txt(), font='helvetica 14', width=5,
               command=lambda: try_to_play(player, lbl_action))
    btn_choose = Button(window, text=Msgs.choose_button_txt(), font='helvetica 14', width=7,
               command=lambda: stop_playback_and_load_file_and_update_labels(sound_dict, player,
               lbl_file_loaded, lbl_action))
    btn_stop = Button(window, text=Msgs.stop_btn_txt(), font='helvetica 14', width=5,
               command=lambda: player.stop_if_playing())
    btn_reverse = Button(window, text=Msgs.reverse_btn_txt(), font='helvetica 14', width=7,
               command=lambda: stop_playback_reverse_file_and_update_label
               (sounds, player, lbl_action))

    widget_pairs = {
        WidgetNames.LBL_FILE_LOADED: lbl_file_loaded,
        WidgetNames.LBL_ACTION: lbl_action,
        WidgetNames.BTN_PLAY: btn_play,
        WidgetNames.BTN_CHOOSE: btn_choose,
        WidgetNames.BTN_STOP: btn_stop,
        WidgetNames.BTN_REVERSE: btn_reverse
    }

    return widget_pairs


def root_widgets_to_grid(widgets):
    widgets[WidgetNames.LBL_FILE_LOADED]    .grid(row=0, column=0, columnspan=3)
    widgets[WidgetNames.LBL_ACTION]         .grid(row=1, column=0, columnspan=3, pady=8)
    widgets[WidgetNames.BTN_CHOOSE]         .grid(row=2, column=1)
    widgets[WidgetNames.BTN_PLAY]           .grid(row=3, column=0)
    widgets[WidgetNames.BTN_REVERSE]        .grid(row=3, column=1)
    widgets[WidgetNames.BTN_STOP]           .grid(row=3, column=2)
    # TODO: Bring everything into vertical alignment. It's askew right now


def root_grid_config(root):
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)


def try_to_play(player, lbl):
    if player.sound:
        player.play()
    else:
        lbl.config(text="Nothing to play. Load a file!")


def stop_playback_and_load_file_and_update_labels(sound_dict, player, loaded_lbl, reversed_file_lbl):
    player.stop_if_playing()

    path = get_file_path_from_user()
    if path:  # If user didn't click cancel
        sound = SoundBuilder.build_sound_from_path(path)
        sound_dict.add("original", sound)
        player.sound = sound

        file_name = TextEditor.get_file_name_from_path(path)
        fit_name = TextEditor.write_file_loaded_msg(file_name, loaded_lbl)
        loaded_lbl.config(text=fit_name)
        reversed_file_lbl.config(text="")


def get_file_path_from_user():
    return filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])


def seg_to_wave_obj(seg: AudioSegment):
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def stop_playback_reverse_file_and_update_label(sounds, player, reversed_lbl):
    player.stop_if_playing()
    if "reversed" in sounds:
        if player.sound == sounds["reversed"]:
            player.sound = sounds["original"]
            reversed_lbl.config(text="Unreversed file!")
        elif player.sound == sounds["original"]:
            player.sound = sounds["reversed"]
            reversed_lbl.config(text="Reversed file!")
    elif player.sound:
        reversed_seg = AudioSegment.from_file(player.sound.path).reverse()
        reversed_sound = SoundBuilder.build_sound_from_audio_seg(reversed_seg)
        sounds["reversed"] = reversed_sound
        player.sound = reversed_sound
        reversed_lbl.config(text="Reversed file!")
    else:
        reversed_lbl.config(text="No file to reverse!")


def main():
    root = create_root_window()
    player = SoundPlayer()
    s_dict = SoundDict()
    w_dict = WidgetDict()
    w_dict.widgets = fill_widget_dict(root, player, s_dict)
    root_widgets_to_grid(w_dict.widgets)

    mainloop()


main()

# TODO: Download button!
