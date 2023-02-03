from pydub import AudioSegment
from simpleaudio import WaveObject
import warnings

from Sound import Sound


class SoundBuilder:

    @staticmethod
    def get_audio_seg(path):
        return AudioSegment.from_file(path)

    @staticmethod
    def to_wave_obj(seg: AudioSegment):
        return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)

    @staticmethod
    def build_sound_from_path(sound, path):     # TODO: Fix this and others so they don't have to take a sound
        sound.audio_seg = SoundBuilder.get_audio_seg(path)
        sound.wave_obj = SoundBuilder.to_wave_obj(sound.audio_seg)
        return sound

    @staticmethod
    def build_sound_from_audio_seg(seg: AudioSegment):
        sound = Sound()
        sound.path = ""
        sound.audio_seg = seg
        sound.wave_obj = SoundBuilder.to_wave_obj(seg)
        return sound

    @staticmethod
    def build_missing_sound_parts(sound):
        if sound.path:
            if not sound.audio_seg:
                sound.audio_seg = SoundBuilder.get_audio_seg(sound.path)
            if not sound.wave_obj:
                sound.wave_obj = SoundBuilder.to_wave_obj(sound.audio_seg)
        if sound.audio_seg and not sound.wave_obj:
            sound.wave_obj = SoundBuilder.to_wave_obj(sound.audio_seg)
        if not sound.path and not sound.audio_seg:
            warnings.warn('Warning: SoundBuilder.build_missing_sound_parts() couldn\'t build anything, because it was\n'
                          'passed a sound that had neither a path nor an AudioSegment.\n')
        return sound

    @staticmethod
    def reverse(sound: Sound):
        if not sound.path and not sound.audio_seg:
            raise ValueError("SoundBuilder.reverse() was called with a Sound as argument, but the Sound contained\n"
                             "neither a path nor an AudioSegment, so the operation couldn't be performed.")
        if not sound.audio_seg:
            sound.audio_seg = SoundBuilder.get_audio_seg(sound.path)

        backwards_seg = sound.audio_seg.reverse()
        return SoundBuilder.build_sound_from_audio_seg(backwards_seg)

# TODO: make reverse() function where arg is path, and another where arg is audio_seg
