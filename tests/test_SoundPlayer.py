import time
import unittest

from pydub import AudioSegment
from simpleaudio import WaveObject

from source.Sound import Sound as Sound
from source.SoundPlayer import SoundPlayer as SoundPlayer


def play_file(player, path):
    seg = AudioSegment.from_file(path)
    wave_obj = WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)
    player.sound = Sound(wave_obj=wave_obj)
    player.play()


class MyTestCase(unittest.TestCase):

    def test_sound_plays(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Bob Marley - Is This Love.mp3")
        self.assertTrue(player.play_obj.is_playing())

    def test_long_sound_plays(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Nina Simone - Sinnerman.mp3")
        self.assertTrue(player.play_obj.is_playing())

    def test_short_sound_plays(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Mario coin.mp3")
        self.assertTrue(player.play_obj.is_playing())

    def test_playback_stops(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Bob Marley - Is This Love.mp3")
        player.stop_if_playing()
        time.sleep(0.2)     # Stopping playback takes a moment, it seems, so we wait.
        self.assertFalse(player.play_obj.is_playing())

    def test_play_stop_play_again(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Bob Marley - Is This Love.mp3")
        player.stop_if_playing()
        time.sleep(0.2)
        player.play()
        self.assertTrue(player.play_obj.is_playing())

    def test_no_overlapping_playbacks(self):
        player = SoundPlayer()
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Bob Marley - Is This Love.mp3")
        first_playback = player.play_obj
        play_file(player, "/Users/sergiojthompson/Documents/programs/sonic surge/test_files/Joy Division - Disorder.mp3")
        time.sleep(0.2)
        self.assertFalse(first_playback.is_playing())


def player_suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_sound_plays'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(player_suite())
