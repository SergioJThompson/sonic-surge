from pydub import AudioSegment
from simpleaudio import WaveObject


class Sound:

    def __init__(self, path: str = "", audio_seg: AudioSegment = None, wave_obj: WaveObject = None):
        self.path = path
        self.audio_seg = audio_seg
        self.wave_obj = wave_obj

# TODO: Make a system of booleans that indicate whether this sound is reversed or not, and that can be expanded
    # TODO: to accomodate other attributes like sped up, phased, etc.
