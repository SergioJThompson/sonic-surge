class SoundPlayer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.sound = None
        self.play_obj = None

    def play(self):
        self.stop_if_playing()
        if self.sound and self.sound.wave_obj:
            self.play_obj = self.sound.wave_obj.play()

    def stop_if_playing(self):
        if self.sound and self.play_obj and self.play_obj.is_playing():
            self.play_obj.stop()

    # TODO: Fix bug: 'Sound' object has no attribute 'play_obj' when you click Play
    # TODO: Implement pausing using other library
