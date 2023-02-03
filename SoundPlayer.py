class SoundPlayer:

    def __init__(self):
        self.sound = None
        self.play_obj = None
        self.play_obj = None
        self.reversed_wave_obj = None
        self.time_last_playback_started = None
        self.time_spent_playing_back_file = None

        # TODO: Implement pausing using other library
        # TODO: Make all these variables global. We only need one SoundPlayer

    def play(self):
        self.sound.stop_if_playing()
        if self.sound.wave_obj:
            self.play_obj = self.sound.wave_obj.play()

    def stop_if_playing(self):
        if self.sound.is_playing():
            self.play_obj.stop_if_playing()

    def is_playing(self):
        return self.sound and self.sound.play_obj and self.sound.play_obj.is_playing()
