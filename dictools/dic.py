import gspread
from oauth2client.service_account import ServiceAccountCredentials


class DicError(Exception):
    pass


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

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0 or item >= self.__len__():
            raise DicError('expected valid index, got %s' % item)
        return self.dic[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or key >= self.__len__():
            raise DicError('expected valid index, got %s' % key)

        if len(value) != 2:
            raise DicError('expected list of 2, got %s' % value)

        self.dic[key] = value

    @classmethod
    def from_google_spreadsheet(cls, credentials, url=None, name=None, sheet_index=0):
        if not (url is None) ^ (name is None):
            raise DicError('please provide either url or name')

        try:
            gc = gspread.authorize(credentials)
        except Exception as e:
            raise DicError('failed establishing google credentials: %s' % e)

        try:
            spreadsheet = gc.open_by_url(url) if url is not None else gc.open(name)
            worksheet = spreadsheet.get_worksheet(sheet_index)
        except Exception as e:
            raise DicError('failed opening spreadsheet: %s' % e)

        list_of_rows = worksheet.get_all_values()
        try:
            lng_src = list_of_rows[0][0]
            lng_dst = list_of_rows[0][1]
            dic = [(row[0], row[1]) for row in list_of_rows[1:]]
            return Dic(lng_src, lng_dst, dic)
        except Exception as e:
            raise DicError('error parsing spreadsheet: %s' % e)

    @classmethod
    def _credentials(cls, signed_credentials_path):
        scope = ['https://spreadsheets.google.com/feeds']
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(signed_credentials_path, scope)
        except Exception as e:
            raise DicError('failed establishing google credentials: %s' % e)

        return credentials
