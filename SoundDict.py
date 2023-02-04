# TODO: Make it so clicking reverse for the second time brings up the original file

class SoundDict:
    sounds = {}

    @classmethod
    def add(cls, name, sound):
        cls.sounds[name] = sound
