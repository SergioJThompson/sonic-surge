# TODO: Set action label text to "" when file loaded. Or maybe "File loaded!"

from tkinter import filedialog
from os.path import expanduser

from SoundBuilder import SoundBuilder
from TextEditor import TextEditor
from MsgLibrary import MsgLibrary as Msgs
from Tags import Tags


class Operator:

    @staticmethod
    def stop_playback_and_load_file_and_update_labels(bank, player, loaded_lbl, reversed_file_lbl):
        player.stop_if_playing()

        path = filedialog.askopenfilename(initialdir=expanduser("/Users/sergiojthompson/Documents/programs/sonic-surge/test_files"), filetypes=[("MP3 files", "*.mp3")])
        # TODO: Change that directory to ~/Music/ when program is finished
        if path:  # If user didn't click cancel
            sound = SoundBuilder.build_sound_from_path(path)
            bank.clear()
            bank.add(sound)
            player.sound = sound

            file_name = TextEditor.get_file_name_from_path(path)
            fit_name = TextEditor.write_file_loaded_msg(file_name, loaded_lbl)
            loaded_lbl.config(text=fit_name)
            reversed_file_lbl.config(text="File loaded!")

    @staticmethod
    def stop_playback_and_alter_frames_and_update_label(bank, player, action_lbl):
        if not player.sound:
            action_lbl.config(text="No file to modify!")
            return

        player.stop_if_playing()

        altered_tags = set(player.sound.tags)
        SoundBuilder.add_or_remove(Tags.FRAMES_LOWERED, altered_tags)
        if bank.has_sound_with_exact_tags(altered_tags):
            player.sound = bank.get_sound_with_exact_tags(altered_tags)
        else:
            lowered_sound = SoundBuilder.lower_frames(player.sound)
            bank.add(lowered_sound)
            player.sound = lowered_sound

        action_lbl.config(text="Altered sample rate of file!")

    @staticmethod
    def stop_playback_and_reverse_file_and_update_label(bank, player, action_lbl):
        if not player.sound:
            action_lbl.config(text="No file to reverse!")
            return

        player.stop_if_playing()

        reversed_tags = set(player.sound.tags)
        SoundBuilder.add_or_remove(Tags.REVERSED, reversed_tags)
        if bank.has_sound_with_exact_tags(reversed_tags):
            player.sound = bank.get_sound_with_exact_tags(reversed_tags)
        else:
            reversed_sound = SoundBuilder.reverse(SoundBuilder.build_sound_from_audio_seg(player.sound.audio_seg))
            bank.add(reversed_sound)
            player.sound = reversed_sound

        action_lbl.config(text="Reversed file!")

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
