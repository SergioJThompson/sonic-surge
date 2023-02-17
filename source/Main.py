# TODO: Make it so a file can have multiple attributes [e.g. reversed AND frames lowered]
# TODO: Implement unit tests for labels.
# TODO: Implement unit tests for playback and reverse playback.

from tkinter import *

from MsgLibrary import MsgLibrary as Msgs
from SoundDict import SoundDict
from SoundPlayer import SoundPlayer
from WidgetDict import WidgetDict
from WidgetNames import WidgetNames
from source.Operator import Operator


def create_root_window():
    root = Tk()
    window_width = 300
    window_height = 147
    root.minsize(window_width, window_height)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")
    return root


def write_widget_dict(window, player, sound_dict):
    lbl_file_loaded = Label(window, text=Msgs.no_file_loaded(), justify=CENTER, font='helvetica 14 bold')
    lbl_action = Label(window, justify=CENTER, font='helvetica 14')
    btn_play = Button(window, text=Msgs.play_btn_txt(), font='helvetica 14', width=5,
                      command=lambda: Operator.try_to_play_and_update_lbl(player, lbl_action))
    btn_choose = Button(window, text=Msgs.choose_button_txt(), font='helvetica 14', width=7,
               command=lambda: Operator.stop_playback_and_load_file_and_update_labels(sound_dict, player,
               lbl_file_loaded, lbl_action))
    btn_stop = Button(window, text=Msgs.stop_btn_txt(), font='helvetica 14', width=5,
               command=lambda: Operator.stop_playback_and_update_label(player, lbl_action))
    btn_reverse = Button(window, text=Msgs.reverse_btn_txt(), font='helvetica 14', width=7,
               command=lambda: Operator.stop_playback_and_reverse_file_and_update_label
               (sound_dict, player, lbl_action))
    btn_pause = Button(window, text=Msgs.pause_btn_txt(), font='helvetica 14', width=7)
    btn_lower_frames = Button(window, text=Msgs.lower_sample_rate(), font='helvetica 14', width=5,
                              command=lambda: Operator.stop_playback_and_lower_frames_and_update_label
                (sound_dict, player, lbl_action))
    # TODO: Undo all changes button
    widget_pairs = {
        WidgetNames.LBL_FILE_LOADED: lbl_file_loaded,
        WidgetNames.LBL_ACTION: lbl_action,
        WidgetNames.BTN_PLAY: btn_play,
        WidgetNames.BTN_CHOOSE: btn_choose,
        WidgetNames.BTN_STOP: btn_stop,
        WidgetNames.BTN_REVERSE: btn_reverse,
        WidgetNames.BTN_PAUSE: btn_pause,
        WidgetNames.BTN_FRAMES: btn_lower_frames
    }

    return widget_pairs


def root_widgets_to_grid(widgets):
    widgets[WidgetNames.LBL_FILE_LOADED]    .grid(row=0, column=0, columnspan=3)
    widgets[WidgetNames.LBL_ACTION]         .grid(row=1, column=0, columnspan=3, pady=8)
    widgets[WidgetNames.BTN_CHOOSE]         .grid(row=2, column=1, padx=28)
    widgets[WidgetNames.BTN_PLAY]           .grid(row=3, column=0)
    widgets[WidgetNames.BTN_STOP]           .grid(row=3, column=2)
    widgets[WidgetNames.BTN_PAUSE]          .grid(row=3, column=1)
    widgets[WidgetNames.BTN_REVERSE]        .grid(row=4, column=1)
    widgets[WidgetNames.BTN_FRAMES]         .grid(row=4, column=2)


def root_grid_config(root):
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)


def main():
    root = create_root_window()
    player = SoundPlayer()
    s_dict = SoundDict()
    w_dict = WidgetDict()
    w_dict.widgets = write_widget_dict(root, player, s_dict)
    root_widgets_to_grid(w_dict.widgets)

    mainloop()


main()

# TODO: Download button!
