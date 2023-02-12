# TODO: Make it so clicking reverse for the second time brings up the original file

class SoundDict:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.sounds = {}

    def add(self, i, sound):
        self.sounds[i] = sound

    def clear(self):
        self.sounds = {}
