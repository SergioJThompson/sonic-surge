from pydub import AudioSegment
from simpleaudio import WaveObject

from Sound import Sound


class SoundBuilder:

    @staticmethod
    def get_audio_seg(path):
        return AudioSegment.from_file(path)

    @staticmethod
    def to_wave_obj(seg: AudioSegment):
        return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)

    @staticmethod
    def build_sound_from_path(path):
        seg = SoundBuilder.get_audio_seg(path)
        wave_obj = SoundBuilder.to_wave_obj(seg)
        return Sound(path=path, audio_seg=seg, wave_obj=wave_obj)

    @staticmethod
    def build_sound_from_audio_seg(seg: AudioSegment):
        wave_obj = SoundBuilder.to_wave_obj(seg)
        return Sound(audio_seg=seg, wave_obj=wave_obj)

    @staticmethod
    def reverse(sound: Sound):
        if not sound.path and not sound.audio_seg:
            raise ValueError("The object passed to SoundBuilder.reverse() had\n"
                             "neither a path nor an AudioSegment, so the operation couldn't be performed.")
        if not sound.audio_seg:
            sound.audio_seg = SoundBuilder.get_audio_seg(sound.path)

        backwards_seg = sound.audio_seg.reverse()
        return SoundBuilder.build_sound_from_audio_seg(backwards_seg)
