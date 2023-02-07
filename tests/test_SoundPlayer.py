import unittest

import pydub
from pydub import AudioSegment
from simpleaudio import WaveObject

from source.Sound import Sound as Sound
from source.SoundBuilder import SoundBuilder as SoundBuilder
from source.SoundPlayer import SoundPlayer as SoundPlayer


class MyTestCase(unittest.TestCase):

    def test_sound_plays(self):
        seg = AudioSegment.from_file("/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Bob Marley - Is This Love.mp3", "mp3")
        wave_obj = WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)
        sound = Sound(wave_obj=wave_obj)
        player = SoundPlayer()
        player.sound = sound
        player.play()
        self.assertTrue(player.play_obj.is_playing())


def player_suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_sound_plays'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(player_suite())
