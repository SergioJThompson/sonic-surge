# TODO: Set action label text to "" when file loaded. Or maybe "File loaded!"

from pydub import AudioSegment
from tkinter import filedialog
from os.path import expanduser

from SoundBuilder import SoundBuilder
from TextEditor import TextEditor
from MsgLibrary import MsgLibrary as Msgs


class Operator:

    @staticmethod
    def stop_playback_and_load_file_and_update_labels(sound_dict, player, loaded_lbl, reversed_file_lbl):
        player.stop_if_playing()

        path = filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])
        if path:  # If user didn't click cancel
            sound = SoundBuilder.build_sound_from_path(path)
            sound_dict.clear()
            sound_dict.add("original", sound)
            player.sound = sound

            file_name = TextEditor.get_file_name_from_path(path)
            fit_name = TextEditor.write_file_loaded_msg(file_name, loaded_lbl)
            loaded_lbl.config(text=fit_name)
            reversed_file_lbl.config(text="")

    @staticmethod
    def stop_playback_and_reverse_file_and_update_label(sounds, player, reversed_lbl):
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

    @staticmethod
    def stop_playback_and_update_label(player, lbl):
        if player.is_playing():
            player.stop()
            lbl.config(text=Msgs.stopped_playback())
        else:
            lbl.config(text=Msgs.no_playback_to_stop())

    @staticmethod
    def try_to_play_and_update_lbl(player, lbl):
        if player.sound:
            player.play()
            lbl.config(text=Msgs.playing())
        else:
            lbl.config(text=Msgs.no_file_to_play())
        # TODO: Say "Finished playing" when file finishes playing
