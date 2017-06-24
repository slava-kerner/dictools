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

    def test_from_google_spreadsheet(self):
        credentials = Dic._credentials('dictools-7bcfbe139da9.json')

        with self.assertRaises(DicError):
            Dic.from_google_spreadsheet(credentials, '', '')

        dic = Dic.from_google_spreadsheet(credentials, name='test_dictools')
        self.assertEqual(dic, self.sample)

        url = 'https://docs.google.com/spreadsheets/d/1yK6uq3e5slF_3EPtIRxcuKMQJrS0Tdhy-D69k-Nx_Mw'
        dic = Dic.from_google_spreadsheet(credentials, url=url)
        self.assertEqual(dic, self.sample)
