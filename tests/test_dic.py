import unittest

from dictools.dic import Dic


class TestDic(unittest.TestCase):

    sample = Dic('fr', 'en', [('moi', 'I'), ('toi', 'you')])

    def test(self):
        self.assertEqual(len(self.sample), 2)
