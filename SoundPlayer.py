class SoundPlayer:
    sound = None
    play_obj = None

    @classmethod
    def play(cls):
        cls.stop_if_playing()
        if cls.sound.wave_obj:
            cls.play_obj = cls.sound.wave_obj.play()

    @classmethod
    def stop_if_playing(cls):
        if cls.sound and cls.sound.play_obj and cls.sound.play_obj.is_playing():    # These all have to be checked, in
                                                                                    # this order, to avoid null point e.
            cls.play_obj.stop()

    # TODO: Fix bug: 'Sound' object has no attribute 'play_obj' when you click Play
    # TODO: Implement pausing using other library
