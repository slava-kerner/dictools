class Dic:
    """ pairs of words in 2 languages. """
    def __init__(self, lng_src=None, lng_dst=None, dic=None):
        """
        :param lng_src: string 
        :param lng_dst: string 
        :param dic: list of pairs of strings
        """
        self.lng_src = lng_src
        self.lng_dst = lng_dst
        self.dic = dic

    def __len__(self):
        return len(self.dic)

    def __eq__(self, other):
        return self.lng_src == other.lng_src and self.lng_dst == other.lng_dst and self.dic == other.dic
