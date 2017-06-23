import unittest

from dictools.dic import Dic


class TestDic(unittest.TestCase):

    sample = Dic('fr', 'en', [('moi', 'I'), ('toi', 'you')])

    def test_len(self):
        self.assertEqual(len(self.sample), 2)

    def test_eq(self):
        self.assertEqual(self.sample, self.sample)
        self.assertNotEqual(self.sample, Dic('fa', 'en', [('moi', 'I'), ('toi', 'you')]))
        self.assertNotEqual(self.sample, Dic('fr', 'es', [('moi', 'I'), ('toi', 'you')]))
        self.assertNotEqual(self.sample, Dic('fr', 'en', [('moI', 'I'), ('toi', 'you')]))
