class SoundMemoryBank:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.sounds = set()

    def add(self, sound):
        self.sounds.add(sound)

    def clear(self):
        self.sounds = set()

    def get_original_sound(self):
        for sound in self.sounds:
            if not sound.tags:
                return sound
        raise Exception("Couldn't get original sound from SoundMemoryBank")

    def get_sound_with_exact_tags(self, tags: set):
        for sound in self.sounds:
            if sound.tags == tags:
                return sound
        raise Exception("Couldn't find a sound in sound bank with tags matching those given as argument")

    def has_sound_with_exact_tags(self, tags: set):
        for sound in self.sounds:
            if sound.tags == tags:
                return True
        return False
