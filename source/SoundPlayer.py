import datetime

from source.SoundBuilder import SoundBuilder


class SoundPlayer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.sound = None
        self.play_obj = None
        self.time_playback_started = None
        self.elapsed_seconds = 0.0

    def play(self):
        self.stop_if_playing()
        if self.sound and self.sound.wave_obj:
            sample_rate = self.sound.audio_seg.frame_rate
            if self.elapsed_seconds > 0:
                unelapsed_audio_seg = self.sound.audio_seg[1000 * self.elapsed_seconds:]
                self.sound.wave_obj = SoundBuilder.to_wave_obj(unelapsed_audio_seg)
            self.time_playback_started = datetime.datetime.now()
            self.play_obj = self.sound.wave_obj.play()

    def stop_if_playing(self):
        if self.is_playing():
            self.play_obj.stop()

    def is_playing(self):
        return self.sound and self.play_obj and self.play_obj.is_playing()

    def stop(self):
        self.play_obj.stop()

    def pause_if_playing(self):
        if self.is_playing():
            self.elapsed_seconds += (abs(self.time_playback_started - datetime.datetime.now())).total_seconds()
            self.play_obj.stop()


# TODO: Implement pausing using other library
