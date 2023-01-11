from tkinter import Button
import simpleaudio
from simpleaudio import WaveObject


class PlayButton(Button):

    def __init__(self, audio_seg, *args, **kwargs):
        self.wave_obj = WaveObject(audio_seg.raw_data, audio_seg.channels, audio_seg.sample_width, audio_seg.frame_rate)
        super().__init__(*args, command=self.play, **kwargs)

    def change_wave_obj_using_audio_seg(self, seg):
        self.wave_obj = WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)

    def play(self):
        simpleaudio.stop_all()
        self.wave_obj.play()
