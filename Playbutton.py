from tkinter import Button
from simpleaudio import WaveObject


class Playbutton(Button):

    def __init__(self, *args, wave_obj=None, **kwargs):
        if wave_obj and type(wave_obj) is not WaveObject:
            raise ValueError("Object not of type WaveObject passed to PlayButton as wave_obj")

        self.wave_obj = wave_obj
        self.play_obj = None
        super().__init__(*args, command=self.play, **kwargs)

    def set_sound(self, wave_obj):
        self.wave_obj = wave_obj

    def play(self):
        self.stop()
        if self.wave_obj:
            self.play_obj = self.wave_obj.play()

    def stop(self):
        if self.is_playing():
            self.play_obj.stop()

    def is_playing(self):
        return self.play_obj and self.play_obj.is_playing()
