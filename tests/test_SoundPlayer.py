import unittest

from source.SoundPlayer import SoundPlayer as SoundPlayer
from source.Sound import Sound as Sound


class MyTestCase(unittest.TestCase):

    def sound_plays(self):
        player = SoundPlayer()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
