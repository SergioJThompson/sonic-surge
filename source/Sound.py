from pydub import AudioSegment
from simpleaudio import WaveObject


class Sound:

    def __init__(self, path: str = "", audio_seg: AudioSegment = None, wave_obj: WaveObject = None, tags: set = None):
        if tags is None:
            tags = set()
        self.path = path
        self.audio_seg = audio_seg
        self.wave_obj = wave_obj
        self.tags = tags
