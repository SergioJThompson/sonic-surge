from tkinter import Button
from pygame import mixer


class PlayButton(Button):
    def __init__(self, sound, *args, **kwargs):
        self.sound = sound
        super().__init__(*args, command=lambda: mixer.Sound(self.sound).play(), **kwargs)
        # TODO: Alter the command so it ends the playback if the file is already playing, so we don't have two
        #  overlapping playbacks.
        # TODO: Alter the command so it waits until the mp3 is done loading to play it. Currently, if a file takes
        #  a moment to load, playback seems to "skip past" the first moment of sound.
