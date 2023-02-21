import datetime

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
        self.time_playback_elapsed = 0

    def play(self):
        self.stop_if_playing()
        if self.sound and self.sound.wave_obj:
            self.play_obj = self.sound.wave_obj.play()
            self.time_playback_started = datetime.datetime.now()

    def stop_if_playing(self):
        if self.is_playing():
            self.play_obj.stop()

    def is_playing(self):
        return self.sound and self.play_obj and self.play_obj.is_playing()

    def stop(self):
        self.play_obj.stop()

# TODO: Implement pausing using other library
