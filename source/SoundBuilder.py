from pydub import AudioSegment
from simpleaudio import WaveObject

from Sound import Sound
from source.Tags import Tags


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
    def make_copy(seg: AudioSegment):
        return AudioSegment(seg.get_array_of_samples(), frame_rate=seg.frame_rate, sample_width=seg.sample_width, channels=seg.channels)

    @staticmethod
    def add_or_remove(tag, tags):
        if tag.value in tags:
            tags.remove(tag.value)
        else:
            tags.add(tag.value)

    @staticmethod
    def reverse(sound: Sound):
        if not sound.audio_seg:
            raise ValueError("Sound has no audio segment")

        reversed_seg = sound.audio_seg.reverse()
        reversed_sound = SoundBuilder.build_sound_from_audio_seg(reversed_seg)
        SoundBuilder.add_or_remove(Tags.REVERSED, reversed_sound.tags)
        return reversed_sound

    @staticmethod
    def lower_frames(sound: Sound):
        if not sound.audio_seg:
            raise ValueError("Sound has no audio segment")

        lowered_seg = SoundBuilder.make_copy(sound.audio_seg).set_frame_rate(8000)
        lowered_sound = SoundBuilder.build_sound_from_audio_seg(lowered_seg)
        SoundBuilder.add_or_remove(Tags.FRAMES_LOWERED, lowered_sound.tags)
        return lowered_sound

