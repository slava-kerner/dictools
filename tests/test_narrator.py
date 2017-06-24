import unittest
import os
from tempfile import TemporaryDirectory

from dictools.narrator import Narrator
from dictools.dic import Dic


class TestNarrator(unittest.TestCase):
    def test_narrate(self):
        narrator = Narrator()
        dic = Dic('fr', 'en', [('moi', 'I'), ('toi', 'you')])

        with TemporaryDirectory() as folder:
            folder = 'tmp2'
            output_path = os.path.join(folder, 'out.mp3')
            narrator.narrate(dic, output_path)
            self.assertTrue(os.path.exists(output_path))
