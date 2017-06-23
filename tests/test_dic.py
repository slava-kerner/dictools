import unittest

from dictools.dic import Dic, DicError


class TestDic(unittest.TestCase):

    def setUp(self):
        self.sample = Dic('fr', 'en', [('moi', 'I'), ('toi', 'you')])

    def test_len(self):
        self.assertEqual(len(self.sample), 2)

    def test_eq(self):
        self.assertEqual(self.sample, self.sample)
        self.assertNotEqual(self.sample, Dic('fa', 'en', [('moi', 'I'), ('toi', 'you')]))
        self.assertNotEqual(self.sample, Dic('fr', 'es', [('moi', 'I'), ('toi', 'you')]))
        self.assertNotEqual(self.sample, Dic('fr', 'en', [('moI', 'I'), ('toi', 'you')]))

    def test_access(self):
        self.sample[1] = ['il', 'he']
        self.assertEqual(self.sample[1], ['il', 'he'])

        for invalid in [-1, 2, 's']:
            with self.assertRaises(DicError):
                print(self.sample[invalid])
            with self.assertRaises(DicError):
                self.sample[invalid] = ('moi', 'I')

