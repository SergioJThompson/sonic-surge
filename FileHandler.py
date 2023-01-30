from pydub import AudioSegment

from simpleaudio import WaveObject


def to_audio_seg(path):
    return AudioSegment.from_file(path)


def to_wave_obj(seg: AudioSegment):
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


class FileHandler:

    def __init__(self, path: str = "", audio_seg: AudioSegment = None, wave_obj: WaveObject = None):
        self.path = path
        self.audio_seg = audio_seg
        self.wave_obj = wave_obj
        self.play_obj = None
        self.time_last_playback_started = None
        self.time_spent_playing_back_file = None
        self.reversed_wave_obj = None

        self.build_missing_sound_parts()

    def build_missing_sound_parts(self):
        if self.path:
            if not self.audio_seg:
                self.audio_seg = to_audio_seg(self.path)
            if not self.wave_obj:
                self.wave_obj = to_wave_obj(self.audio_seg)
        if self.audio_seg and not self.wave_obj:
            self.wave_obj = to_wave_obj(self.audio_seg)

    def build_sound_parts_from_path(self, path):
        self.path = path
        self.audio_seg = to_audio_seg(self.path)
        self.wave_obj = to_wave_obj(self.audio_seg)

    def build_sound_parts_from_audio_seg(self, seg: AudioSegment):
        self.path = ""
        self.audio_seg = seg
        self.wave_obj = to_wave_obj(self.audio_seg)

    def play(self):
        self.stop()
        if self.wave_obj:
            self.play_obj = self.wave_obj.play()

    def stop(self):
        if self.is_playing():
            self.play_obj.stop()

    def is_playing(self):
        return self.play_obj and self.play_obj.is_playing()



# TODO: Implement pausing using other library
